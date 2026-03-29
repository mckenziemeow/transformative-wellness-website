#!/usr/bin/env python3
"""Apply Ageless AI embeds across Transformative Wellness HTML (idempotent)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGELESS = "https://ageless.ai/a/transformativewellness/wellness"

SERVICE_STRIP_FILES = {
    "injectables.html",
    "skin-laser.html",
    "body-weight.html",
    "iv-therapy.html",
    "lashes-smooth.html",
    "concerns.html",
    "services.html",
    "find-your-treatment.html",
}


def asset_prefix(path: Path) -> str:
    depth = len(path.relative_to(ROOT).parts) - 1
    return "../" * depth


def nav_li() -> str:
    return (
        f'                <li><a href="{AGELESS}" class="nav-ageless-link" '
        'target="_blank" rel="noopener noreferrer">AI Treatment Advisor'
        '<span class="nav-ageless-new" aria-hidden="true">NEW</span></a></li>\n'
    )


def footer_block() -> str:
    return f"""            <div class="footer-ageless-cta" role="region" aria-label="AI treatment advisor">
                <h3>Not sure where to start?</h3>
                <p>Our AI Treatment Advisor matches you with treatment ideas based on your goals. Free consultations — <a href="tel:8584440414">(858) 444-0414</a></p>
                <p class="footer-ageless-address">969 Vale Terrace Dr, Suite B · Vista, CA 92084</p>
                <a href="{AGELESS}" class="ageless-footer-btn" target="_blank" rel="noopener noreferrer">Start Your Free Assessment</a>
            </div>

"""


def service_strip() -> str:
    return f"""    <section class="ageless-service-wrap" aria-label="AI treatment advisor">
        <div class="container">
            <div class="ageless-service-cta">
                <p class="ageless-service-q">Wondering if this treatment is right for you?</p>
                <a href="{AGELESS}" class="ageless-service-btn" target="_blank" rel="noopener noreferrer">Take the Free AI Assessment</a>
                <p class="ageless-service-note">See personalized recommendations in minutes · Free consultations · Vista, CA only</p>
            </div>
        </div>
    </section>

"""


def popup_block() -> str:
    return f"""    <div id="ageless-popup" class="ageless-popup" role="dialog" aria-labelledby="ageless-popup-title" aria-modal="false" hidden>
        <button type="button" class="ageless-popup-close" aria-label="Close">&times;</button>
        <h3 id="ageless-popup-title" class="ageless-popup-title">Curious what treatment is right for you?</h3>
        <p class="ageless-popup-text">Our AI advisor analyzes your goals and shows personalized options — free and instant.</p>
        <a href="{AGELESS}" class="ageless-popup-btn" target="_blank" rel="noopener noreferrer">See Your AI Preview →</a>
    </div>

"""


def mobile_block() -> str:
    return f"""    <div class="ageless-mobile-bar" role="region" aria-label="AI treatment preview">
        <a href="{AGELESS}" class="ageless-mobile-bar-link" target="_blank" rel="noopener noreferrer">See Your AI Treatment Preview →</a>
    </div>

"""


def add_css_link(text: str, prefix: str) -> str:
    if "css/ageless.css" in text or "ageless.css" in text:
        return text
    needle = f'    <link rel="stylesheet" href="{prefix}css/style.css">'
    insert = needle + f'\n    <link rel="stylesheet" href="{prefix}css/ageless.css">'
    if needle in text:
        return text.replace(needle, insert, 1)
    return text


def add_nav(text: str) -> str:
    if "nav-ageless-link" in text:
        return text
    li = nav_li()
    reps = [
        (
            '                <li><a href="about.html">About</a></li>\n'
            '                <li><a href="contact.html">Contact</a></li>',
            '                <li><a href="about.html">About</a></li>\n'
            + li
            + '                <li><a href="contact.html">Contact</a></li>',
        ),
        (
            '                <li><a href="../about.html">About</a></li>\n'
            '                <li><a href="../contact.html">Contact</a></li>',
            '                <li><a href="../about.html">About</a></li>\n'
            + li
            + '                <li><a href="../contact.html">Contact</a></li>',
        ),
        (
            '                <li><a href="../about.html">About</a></li>\n'
            '                <li><a href="./">Blog</a></li>',
            '                <li><a href="../about.html">About</a></li>\n'
            + li
            + '                <li><a href="./">Blog</a></li>',
        ),
    ]
    for old, new in reps:
        if old in text:
            return text.replace(old, new, 1)
    return text


def add_footer(text: str, path: Path) -> str:
    if "footer-ageless-cta" in text:
        return text
    marker = '            <div class="footer-bottom">'
    if marker in text:
        return text.replace(marker, footer_block() + marker, 1)
    # Minimal blog article footers
    ghl = "\n\n    <!-- GHL Webchat"
    if ghl in text and path.parent.name == "blog" and path.name != "index.html":
        old = "            </div>\n        </div>\n    </footer>" + ghl
        new = "            </div>\n" + footer_block() + "        </div>\n    </footer>" + ghl
        if old in text:
            return text.replace(old, new, 1)
    return text


def add_service_strip(text: str, path: Path) -> str:
    if "ageless-service-wrap" in text:
        return text
    rel = path.relative_to(ROOT)
    name = rel.name
    parts = rel.parts
    if name == "find-your-treatment.html":
        old = "    </section>\n\n    <!-- Quiz Section -->"
        if old in text:
            return text.replace(old, "    </section>\n\n" + service_strip() + "    <!-- Quiz Section -->", 1)
        return text
    if name not in SERVICE_STRIP_FILES and not (len(parts) >= 2 and parts[0] == "locations"):
        return text
    m = re.search(
        r'(<section class="page-header">[\s\S]*?</section>\s*\n)',
        text,
    )
    if not m:
        return text
    return text.replace(m.group(1), m.group(1) + service_strip(), 1)


def add_hero_index(text: str, path: Path) -> str:
    if path.name != "index.html" or "ageless-hero-cta" in text or "hero--welcome" in text:
        return text
    old = """            <p class="hero-subtitle">Natural results from board-certified experts in Vista, CA</p>

            <div class="hero-buttons">"""
    new = f"""            <p class="hero-subtitle">Natural results from board-certified experts in Vista, CA</p>

            <div class="ageless-hero-cta">
                <a href="{AGELESS}" class="ageless-hero-btn" target="_blank" rel="noopener noreferrer">✨ Discover Your Perfect Treatment — Try Our AI Advisor</a>
                <p class="ageless-hero-note">Free AI-powered treatment assessment · See your preview in minutes · Vista, CA · Free consultations <a href="tel:8584440414">(858) 444-0414</a></p>
            </div>

            <div class="hero-buttons">"""
    return text.replace(old, new, 1)


def add_scripts(text: str, path: Path, prefix: str) -> str:
    if "js/ageless.js" in text or "ageless.js" in text:
        return text
    inj = ""
    if path.name == "index.html":
        inj += popup_block()
    inj += mobile_block()
    ageless_script = f'    <script src="{prefix}js/ageless.js" defer></script>\n'
    main_tag = f'    <script src="{prefix}js/main.js"></script>'
    if main_tag in text:
        return text.replace(main_tag, inj + ageless_script + main_tag, 1)
    # Pages without main.js (some location landers): insert before </body>
    closing = "</body>"
    idx = text.rfind(closing)
    if idx == -1:
        return text
    return text[:idx] + inj + ageless_script + text[idx:]


def patch_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    prefix = asset_prefix(path)
    text = raw
    text = add_css_link(text, prefix)
    text = add_nav(text)
    text = add_footer(text, path)
    text = add_service_strip(text, path)
    text = add_hero_index(text, path)
    text = add_scripts(text, path, prefix)
    if text != raw:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    html_files = list(ROOT.rglob("*.html"))
    n = 0
    for p in sorted(html_files):
        if patch_file(p):
            print("patched", p.relative_to(ROOT))
            n += 1
    print("done,", n, "files changed")


if __name__ == "__main__":
    main()
