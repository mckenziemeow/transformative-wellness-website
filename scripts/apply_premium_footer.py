#!/usr/bin/env python3
"""Replace legacy footers with the Phase 4 premium footer (one-time sync)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAT = re.compile(
    r"(?:<!-- Footer -->\s*)?<footer class=\"footer[^\"]*\"[^>]*>.*?</footer>\s*",
    re.DOTALL,
)


def footer_block(pfx: str, *, blog_nav_link: bool) -> str:
    blog_line = ""
    if blog_nav_link:
        blog_line = '                        <li><a href="index.html">Blog</a></li>\n'
    return f"""    <!-- Footer -->
    <footer class="footer footer-premium">
        <div class="container">
            <div class="footer-grid-premium">
                <div class="footer-brand">
                    <a href="{pfx}index.html" class="footer-logo">
                        <span class="logo-script">Transformative</span>
                        <span class="logo-main">Wellness</span>
                    </a>
                    <p class="footer-tagline">Vista&apos;s Premier Medical Spa — natural injectables, laser, weight care &amp; IV therapy.</p>
                    <div class="footer-social">
                        <a href="https://instagram.com/transformative_wellness" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="https://www.facebook.com/Transformativewellnesscenters/" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
                        <a href="https://www.tiktok.com/search?q=Transformative%20Wellness%20Vista" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                        <a href="https://www.yelp.com/biz/transformative-wellness-vista-3" target="_blank" rel="noopener noreferrer" aria-label="Yelp"><i class="fab fa-yelp"></i></a>
                    </div>
                </div>
                <div class="footer-links">
                    <h4>Quick links</h4>
                    <ul>
                        <li><a href="{pfx}services.html">Services</a></li>
                        <li><a href="{pfx}before-after.html">Results</a></li>
                        <li><a href="{pfx}memberships.html">Memberships</a></li>
                        <li><a href="{pfx}about.html">About</a></li>
                        <li><a href="{pfx}contact.html">Contact</a></li>
{blog_line}                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Top treatments</h4>
                    <ul>
                        <li><a href="{pfx}injectables.html">Botox</a></li>
                        <li><a href="{pfx}injectables.html">Fillers</a></li>
                        <li><a href="{pfx}skin-laser.html">Laser</a></li>
                        <li><a href="{pfx}body-weight.html">Weight loss</a></li>
                        <li><a href="{pfx}iv-therapy.html">IV therapy</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Visit &amp; hours</h4>
                    <p><i class="fas fa-map-marker-alt"></i> 969 Vale Terrace Drive, Suite B<br>Vista, CA 92084</p>
                    <p><i class="fas fa-phone"></i> <a href="tel:+18584440414">(858) 444-0414</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:info@transformativemedspa.com">info@transformativemedspa.com</a></p>
                    <ul class="footer-hours">
                        <li><strong>Mon</strong> 9am – 6pm</li>
                        <li><strong>Wed</strong> 9am – 6pm</li>
                        <li><strong>Fri</strong> 9am – 6pm</li>
                        <li><strong>Sat</strong> 9am – 4pm</li>
                    </ul>
                    <iframe class="footer-map-embed" title="Transformative Wellness on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=969+Vale+Terrace+Dr+Suite+B+Vista+CA+92084&amp;hl=en&amp;z=14&amp;output=embed"></iframe>
                </div>
            </div>
            <div class="footer-financing-row">
                <span>Financing:</span>
                <span>Cherry</span>
                <span>·</span>
                <span>CareCredit</span>
                <span>·</span>
                <span>Affirm</span>
            </div>
            <div class="footer-ageless-cta" role="region" aria-label="AI treatment advisor">
                <h3>Not sure where to start?</h3>
                <p>Our AI Treatment Advisor matches you with treatment ideas based on your goals. Free consultations — <a href="tel:+18584440414">(858) 444-0414</a></p>
                <p class="footer-ageless-address">969 Vale Terrace Dr, Suite B · Vista, CA 92084</p>
                <a href="https://ageless.ai/a/transformativewellness/transformation" class="ageless-footer-btn" target="_blank" rel="noopener noreferrer">Start Your Free Assessment</a>
            </div>

            <div class="footer-bottom">
                <p>&copy; 2026 Transformative Wellness. All rights reserved.</p>
                <div class="footer-legal">
                    <a href="{pfx}privacy-policy.html">Privacy</a>
                    <a href="{pfx}terms-of-service.html">Terms</a>
                    <a href="{pfx}medical-disclaimer.html">HIPAA</a>
                    <a href="{pfx}accessibility.html">Accessibility</a>
                </div>
            </div>
        </div>
    </footer>

"""


def patch(path: Path, pfx: str, blog_nav_link: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    m = PAT.search(text)
    if not m:
        print("skip (no match):", path, file=sys.stderr)
        return False
    new = PAT.sub(footer_block(pfx, blog_nav_link=blog_nav_link), text, count=1)
    path.write_text(new, encoding="utf-8")
    print("ok", path)
    return True


def main() -> None:
    for p in sorted(ROOT.glob("*.html")):
        patch(p, "", blog_nav_link=False)

    blog = ROOT / "blog"
    if blog.is_dir():
        for p in sorted(blog.glob("*.html")):
            patch(p, "../", blog_nav_link=p.name != "index.html")

    loc = ROOT / "locations"
    if loc.is_dir():
        for p in sorted(loc.glob("*.html")):
            patch(p, "../", blog_nav_link=False)


if __name__ == "__main__":
    main()
