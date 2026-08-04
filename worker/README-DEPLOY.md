# Contact form proxy — deploy steps

The Worker is written and committed but **not wired up yet**. contact.html still posts
straight to the GoHighLevel hook, exactly as it did before, so the live form is unaffected
until every step below is done.

Do them in this order. Cutting over before the route exists means every submission 404s
and you lose *all* leads, not just bots.

## 1. Create the Turnstile widget

Cloudflare dashboard → **Turnstile** → Add widget, domain `transformativemedspa.com`.
You get two keys:

- **Site key** — public, goes in contact.html
- **Secret key** — never in the repo, set as a Worker secret in step 2

## 2. Deploy the Worker and set the secret

```
cd worker
npx wrangler deploy
npx wrangler secret put TURNSTILE_SECRET
```

The second command prompts for the secret key. Paste it there — it is never written to
a file.

## 3. Route /api/contact to the Worker

Uncomment the `[[routes]]` block in `wrangler.toml`, then `npx wrangler deploy` again.

If transformativemedspa.com is not on this Cloudflare zone, skip the route and use the
`*.workers.dev` URL as the form action in step 4 instead. CORS is already handled —
`ALLOWED_ORIGIN` in wrangler.toml is set to the site origin.

## 4. Switch the form over (three edits in contact.html)

1. Form action → `/api/contact` (or the workers.dev URL)
2. Uncomment the `<div class="cf-turnstile">` block and paste the **site key** in place
   of `TURNSTILE_SITE_KEY_HERE`
3. Uncomment the Turnstile `<script>` tag near the bottom

The fetch handler self-activates: it checks for `/api/contact` in the form action and
stays out of the way until it is there.

## 5. Verify

Submit a real test from the live page, then confirm in GHL that the contact arrived
tagged `verified_human`. Then try POSTing to the hook URL directly with curl — it should
still work (GHL accepts anything), which is exactly why step 4's job is removing that URL
from public page source.

## What this fixes

The GHL hook URL used to sit in page source. Bots POSTed to it directly without ever
loading the page, so no client-side protection could have stopped them — creating junk
contacts *and* junk pipeline opportunities. Evidence in the 2026-08-04 audit: nameless
submissions through a Google Translate proxy from a single IP, and a contact-form lead
from an AWS datacenter IP running a Linux desktop user agent.
