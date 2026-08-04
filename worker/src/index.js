/**
 * Contact form proxy for transformativemedspa.com
 *
 * Why this exists: the contact form used to POST directly to a public,
 * unauthenticated GoHighLevel hook whose URL sat in the page source. Bots found it
 * and submitted straight to the endpoint, creating junk contacts AND junk pipeline
 * opportunities in GHL (see the 2026-08-04 pipeline audit).
 *
 * This Worker keeps the hook URL server-side and refuses anything that fails
 * Turnstile or trips the honeypot. Client-side checks alone would not help — a bot
 * that already knows the hook URL never loads the page.
 *
 * Secrets/vars (set via `wrangler secret put` / wrangler.toml):
 *   TURNSTILE_SECRET  - Cloudflare Turnstile secret key   (secret)
 *   GHL_HOOK_URL      - the GoHighLevel inbound webhook   (var)
 *   ALLOWED_ORIGIN    - site origin allowed to POST here  (var)
 */

const TURNSTILE_VERIFY = 'https://challenges.cloudflare.com/turnstile/v0/siteverify';

function cors(origin) {
  return {
    'Access-Control-Allow-Origin': origin,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Vary': 'Origin',
  };
}

function json(body, status, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...cors(origin) },
  });
}

export default {
  async fetch(request, env) {
    const origin = env.ALLOWED_ORIGIN || 'https://transformativemedspa.com';

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: cors(origin) });
    }
    if (request.method !== 'POST') {
      return json({ ok: false, error: 'Method not allowed' }, 405, origin);
    }

    // Only accept submissions that came from our own site.
    const reqOrigin = request.headers.get('Origin');
    if (reqOrigin && reqOrigin !== origin) {
      return json({ ok: false, error: 'Bad origin' }, 403, origin);
    }

    let form;
    try {
      form = await request.formData();
    } catch {
      return json({ ok: false, error: 'Malformed submission' }, 400, origin);
    }

    // 1. Honeypot. Real browsers leave this empty; naive bots fill every field.
    //    Return 200 so the bot believes it succeeded and does not retry/adapt.
    if ((form.get('company_website') || '').toString().trim() !== '') {
      return json({ ok: true }, 200, origin);
    }

    // 2. Turnstile, verified server-side. This is the check a direct-to-endpoint
    //    bot cannot fake, because it never rendered the widget.
    const token = form.get('cf-turnstile-response');
    if (!token) {
      return json({ ok: false, error: 'Verification missing' }, 400, origin);
    }

    const verifyBody = new FormData();
    verifyBody.append('secret', env.TURNSTILE_SECRET);
    verifyBody.append('response', token);
    const ip = request.headers.get('CF-Connecting-IP');
    if (ip) verifyBody.append('remoteip', ip);

    const verifyRes = await fetch(TURNSTILE_VERIFY, { method: 'POST', body: verifyBody });
    const verify = await verifyRes.json();
    if (!verify.success) {
      return json({ ok: false, error: 'Verification failed' }, 403, origin);
    }

    // 3. Minimum sanity. Bots that clear the above still tend to send junk.
    const first = (form.get('first_name') || '').toString().trim();
    const email = (form.get('email') || '').toString().trim();
    const phone = (form.get('phone') || '').toString().trim();
    if (!first || !email || !phone) {
      return json({ ok: false, error: 'Missing required fields' }, 400, origin);
    }
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(email)) {
      return json({ ok: false, error: 'Invalid email' }, 400, origin);
    }

    // 4. Forward to GoHighLevel. Drop the Turnstile token and honeypot — GHL has
    //    no use for them and they would land in custom fields as noise.
    const payload = new FormData();
    for (const [key, value] of form.entries()) {
      if (key === 'cf-turnstile-response' || key === 'company_website') continue;
      payload.append(key, value);
    }
    payload.append('verified_human', 'true');

    const ghl = await fetch(env.GHL_HOOK_URL, { method: 'POST', body: payload });
    if (!ghl.ok) {
      // Surface the failure rather than showing a false success — a silently lost
      // lead is worse than an error the visitor can act on.
      return json({ ok: false, error: 'Could not deliver. Please call us.' }, 502, origin);
    }

    return json({ ok: true }, 200, origin);
  },
};
