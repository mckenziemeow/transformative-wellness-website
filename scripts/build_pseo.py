#!/usr/bin/env python3
"""Generate service x city programmatic SEO pages for Transformative Wellness.

Pattern: /[service]-[city]-ca (e.g. /botox-carlsbad-ca)
- Core services (tier="core") generate against ALL cities (broad coverage).
- Secondary services (tier="secondary") generate against the top-5 nearest cities only
  (lighter coverage to avoid thin-content risk for lower-volume queries).

Inputs: SERVICES and CITIES dicts below.
Output: HTML files at repo root + sitemap fragment at scripts/pseo-sitemap-entries.xml.
"""
from pathlib import Path
import json
import html

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT
SITEMAP_FRAGMENT = REPO_ROOT / "scripts" / "pseo-sitemap-entries.xml"

PHONE = "(858) 444-0414"
PHONE_E164 = "+18584440414"
ADDR_STREET = "969 Vale Terrace Drive, Suite B"
ADDR_CITY = "Vista"
ADDR_ZIP = "92084"
BOOK_URL = "https://www.mypatientvisit.com/onlinescheduling/#/scheduler/schedule?practiceid=e47fce2c-cb7d-4f15-9af0-ff7c5ea03744"

# Cities flagged as "top 5" get secondary-service pages too. By proximity + population.
TOP_CITY_SLUGS = {"vista", "carlsbad", "san-marcos", "oceanside", "escondido"}

SERVICES = [
    # ---- CORE / HIGH-PROFIT (10 cities each) ----
    {
        "slug": "botox", "tier": "core",
        "name": "Botox", "h1_phrase": "Botox in {city}, CA",
        "title_label": "Botox & Neurotoxin",
        "category": "Injectables", "internal_link": "injectables.html",
        "short": "smooth wrinkles with FDA-approved neurotoxin",
        "intro": (
            "Botox (onabotulinumtoxinA) is the gold-standard neurotoxin for softening expression "
            "lines on the forehead, between the brows (11s), and around the eyes (crow's feet). "
            "At Transformative Wellness, our injectors are trained to deliver natural, refreshed "
            "results — not the frozen look."
        ),
        "areas": [
            "Forehead lines (frontalis)", "Glabellar lines (11s between brows)",
            "Crow's feet (orbicularis oculi)", "Bunny lines (nasal scrunch)",
            "Brow lift (microbotox)", "Jaw slimming / masseter",
            "Lip flip", "Neck bands (platysmal)",
        ],
        "session_minutes": "15-30",
        "downtime": "None — return to normal activity immediately",
        "results_timing": "Begin in 3-5 days, fully set at 14 days, last 3-4 months",
        "good_candidate": "Adults 25+ who want to soften dynamic wrinkles or prevent new ones",
        "faqs": [
            ("How many units of Botox do I need?",
             "Most patients receive 40-64 units for full upper-face treatment (forehead, 11s, crow's feet). "
             "Smaller treatments like a lip flip use just 4-6 units. Your injector will quote exact units after assessing your muscle strength and goals."),
            ("Does Botox hurt?",
             "The needles are very fine — most patients describe it as a quick pinch. We can apply topical numbing or ice for sensitive areas. "
             "Most appointments take 15-30 minutes including consult."),
            ("Botox vs. Dysport vs. Daxxify — which is right for me?",
             "Botox is the most studied; Dysport spreads slightly more (great for crow's feet); Daxxify lasts up to 6 months. "
             "We carry all three so we can match the product to your face and goals."),
        ],
    },
    {
        "slug": "laser-hair-removal", "tier": "core",
        "name": "Laser Hair Removal", "h1_phrase": "Laser Hair Removal in {city}, CA",
        "title_label": "Laser Hair Removal",
        "category": "Skin & Laser", "internal_link": "skin-laser.html",
        "short": "permanently reduce unwanted hair with medical-grade lasers",
        "intro": (
            "Laser hair removal uses targeted light to disable hair follicles, producing long-lasting "
            "reduction across the body and face. Our medical-grade platform is safe for a wide range of "
            "skin types and is far faster, more comfortable, and more permanent than waxing or shaving."
        ),
        "areas": [
            "Underarms", "Bikini line & Brazilian", "Legs (full or lower)",
            "Back & chest", "Upper lip & chin", "Sideburns & cheeks",
            "Stomach & treasure trail", "Arms & shoulders",
        ],
        "session_minutes": "15-60 depending on area",
        "downtime": "Mild redness for a few hours — back to normal same day",
        "results_timing": "Most patients see 70-90% reduction after 6-8 sessions spaced 4-6 weeks apart",
        "good_candidate": "Adults with unwanted hair on any body area; effective across most skin types",
        "faqs": [
            ("How many laser hair removal sessions will I need?",
             "Most areas require 6-8 sessions spaced 4-6 weeks apart for optimal reduction. Hormonal areas (face, chin) sometimes benefit from "
             "a few extra. Maintenance is typically 1-2 sessions per year."),
            ("Does laser hair removal hurt?",
             "Most patients describe it as a quick rubber-band snap. Our platform has built-in cooling and we offer numbing cream for "
             "sensitive areas like the bikini or face."),
            ("Can I shave between sessions?",
             "Yes — shaving between treatments is encouraged. Do not wax, pluck, or use depilatory creams; the laser needs the hair root "
             "intact in the follicle."),
        ],
    },
    {
        "slug": "rf-microneedling", "tier": "core",
        "name": "RF Microneedling", "h1_phrase": "RF Microneedling in {city}, CA",
        "title_label": "RF Microneedling",
        "category": "Skin & Laser", "internal_link": "skin-laser.html",
        "short": "tighten skin and erase texture issues with radiofrequency microneedling",
        "intro": (
            "RF microneedling combines two proven technologies — micro-channels in the skin and "
            "radiofrequency energy delivered deep into the dermis — to remodel collagen, tighten "
            "skin, smooth acne scars, and refine texture. Results build over 3-6 months as new collagen forms."
        ),
        "areas": [
            "Full face (texture, pores, fine lines)", "Neck & jawline (skin laxity)",
            "Décolletage", "Acne scarring", "Stretch marks (body)",
            "Hands", "Above-knee laxity", "Submental (under chin)",
        ],
        "session_minutes": "45-75 plus 30 min numbing",
        "downtime": "Redness and pinpoint marks for 24-48 hours; back to makeup at 24 hours",
        "results_timing": "Initial glow in 1-2 weeks; full collagen remodeling over 3-6 months. Series of 3 recommended.",
        "good_candidate": "Adults addressing texture, pores, acne scars, or early skin laxity",
        "faqs": [
            ("How is RF microneedling different from regular microneedling?",
             "Standard microneedling creates micro-injuries to stimulate collagen at the surface. RF microneedling adds radiofrequency energy "
             "that heats deeper layers (1.5-3.5mm), driving stronger collagen remodeling and tightening — especially for scarring and laxity "
             "that surface-only treatments can't reach."),
            ("How many RF microneedling sessions do I need?",
             "Most patients see meaningful results from a series of 3 sessions spaced 4-6 weeks apart. Acne scars and stretch marks sometimes "
             "need 4-6. Annual touch-ups maintain results."),
            ("What's the downtime like?",
             "Expect 24-48 hours of redness similar to a moderate sunburn, with pinpoint marks that fade quickly. Most patients return to work "
             "the next day and wear makeup at 24 hours."),
        ],
    },
    {
        "slug": "body-contouring", "tier": "core",
        "name": "Body Contouring", "h1_phrase": "Body Contouring in {city}, CA",
        "title_label": "Body Contouring",
        "category": "Body & Weight Loss", "internal_link": "body-weight.html",
        "short": "non-surgical fat reduction and skin tightening for body sculpting",
        "intro": (
            "Body contouring at Transformative Wellness combines non-surgical fat reduction, skin "
            "tightening, and muscle stimulation to refine areas that diet and exercise can't reach. "
            "Treatments are walk-in, walk-out — no incisions, no anesthesia, minimal downtime."
        ),
        "areas": [
            "Abdomen (upper, lower, full)", "Flanks (love handles)",
            "Inner & outer thighs", "Bra fat & back", "Upper arms",
            "Submental (double chin)", "Knees", "Buttock lift & toning",
        ],
        "session_minutes": "30-60 per area",
        "downtime": "None to minimal — return to normal activity immediately",
        "results_timing": "Visible changes in 6-12 weeks; full results at 3-4 months. Series of 4-6 recommended for most areas.",
        "good_candidate": "Adults within 10-30 lbs of goal weight targeting specific stubborn areas",
        "faqs": [
            ("Is body contouring the same as weight loss?",
             "No — body contouring sculpts specific areas of stubborn fat or laxity. It's most effective for patients already near their goal weight. "
             "If primary goal is significant weight loss, our medical weight loss program (GLP-1) is the right starting point."),
            ("How many body contouring sessions do I need?",
             "Most patients see meaningful changes after a series of 4-6 sessions spaced 1-2 weeks apart. Some areas (chin, arms) respond in 2-3."),
            ("Will the fat come back?",
             "Treated fat cells are eliminated and don't return. However, untreated areas can still gain — maintaining your weight protects "
             "results long-term."),
        ],
    },
    {
        "slug": "glp1-weight-loss", "tier": "core",
        "name": "GLP-1 Weight Loss", "h1_phrase": "GLP-1 Medical Weight Loss in {city}, CA",
        "title_label": "GLP-1 Weight Loss",
        "category": "Body & Weight Loss", "internal_link": "body-weight.html",
        "short": "physician-supervised semaglutide and tirzepatide for sustainable weight loss",
        "intro": (
            "Our medical weight loss program uses GLP-1 medications (semaglutide and tirzepatide) "
            "alongside nutrition coaching and metabolic labs to produce sustained weight loss. "
            "Every patient is screened by our medical director, and dosing is adjusted monthly based "
            "on response and tolerance — not a one-size-fits-all script."
        ),
        "areas": [
            "Semaglutide (compounded)", "Tirzepatide (compounded)",
            "Monthly dose adjustments", "Metabolic labs at intake",
            "Nutrition & macro coaching", "B12 + lipotropic injections (optional)",
            "Maintenance protocols", "Off-ramp planning",
        ],
        "session_minutes": "30 min monthly check-in",
        "downtime": "None — weekly self-injection at home",
        "results_timing": "Most patients lose 1-2% body weight per week, with 10-20% total loss over 6 months",
        "good_candidate": "Adults BMI 27+ (or 25+ with metabolic risk) ready for a 6-12 month medical program",
        "faqs": [
            ("Is GLP-1 weight loss safe?",
             "Semaglutide and tirzepatide have years of safety data in diabetes and obesity. At Transformative Wellness every patient starts with "
             "metabolic labs and screening — we don't prescribe to people who shouldn't take it, and we titrate doses to minimize side effects like nausea."),
            ("How much weight will I lose?",
             "Average loss in clinical trials is 15% body weight on semaglutide and 20-22% on tirzepatide over a year. Real-world results vary based "
             "on starting weight, diet, activity, and how long you stay on the medication."),
            ("What happens when I stop the medication?",
             "Discontinuation without lifestyle change typically leads to partial regain. We build an off-ramp into every program — low-dose maintenance, "
             "nutrition habits, and metabolic monitoring — so the loss sticks."),
        ],
    },
    {
        "slug": "co2-laser", "tier": "core",
        "name": "CO2 Laser", "h1_phrase": "CO2 Laser Resurfacing in {city}, CA",
        "title_label": "CO2 Laser Resurfacing",
        "category": "Skin & Laser", "internal_link": "skin-laser.html",
        "short": "deep skin resurfacing for sun damage, scarring, and texture",
        "intro": (
            "CO2 laser resurfacing is the gold standard for treating sun damage, deep wrinkles, "
            "acne scarring, and texture issues that gentler treatments can't reach. A single full-face "
            "session can deliver years of skin renewal — equivalent to multiple sessions of milder devices."
        ),
        "areas": [
            "Full face resurfacing", "Sun damage & pigment",
            "Deep wrinkles & static lines", "Acne & traumatic scarring",
            "Perioral wrinkles (smoker's lines)", "Neck & décolletage (gentler settings)",
            "Hands (age spots & crepey skin)", "Targeted scars",
        ],
        "session_minutes": "60-90 plus 60 min numbing",
        "downtime": "5-7 days of redness, peeling, and crusting; makeup at day 7-10",
        "results_timing": "Initial new-skin glow at day 7-10; full collagen remodeling over 3-6 months. Often a one-time treatment.",
        "good_candidate": "Adults with significant sun damage, deep wrinkles, or acne scarring who can take a week of downtime",
        "faqs": [
            ("How does CO2 laser compare to RF microneedling?",
             "CO2 laser delivers stronger resurfacing in a single session but requires a week of social downtime. RF microneedling is gentler with "
             "minimal downtime but typically needs a series of 3. We help you choose based on your goals, timeline, and tolerance for healing."),
            ("Will CO2 laser remove my brown spots?",
             "Yes — CO2 vaporizes the damaged surface layer where most pigment sits, dramatically improving sun spots, melasma (carefully), and "
             "uneven tone. Strict sun protection during healing is critical to lock in results."),
            ("How long is CO2 laser downtime?",
             "Expect 5-7 days of social downtime — redness, peeling, crusting. By day 7-10 most patients return to work and wear makeup. Full healing "
             "and pinkness fade over 4-6 weeks."),
        ],
    },
    {
        "slug": "ipl", "tier": "core",
        "name": "IPL Photofacial", "h1_phrase": "IPL Photofacial in {city}, CA",
        "title_label": "IPL Photofacial",
        "category": "Skin & Laser", "internal_link": "skin-laser.html",
        "short": "even skin tone and clear redness with intense pulsed light",
        "intro": (
            "IPL (intense pulsed light) photofacial treats sun damage, brown spots, redness, "
            "rosacea, and broken capillaries in a single 30-minute session — with minimal downtime. "
            "It's our most-requested treatment for patients wanting brighter, more even skin tone "
            "without committing to laser resurfacing."
        ),
        "areas": [
            "Face (sun spots, freckles)", "Neck & décolletage",
            "Diffuse redness & rosacea", "Broken capillaries (telangiectasia)",
            "Hands (age spots)", "Chest & shoulders",
            "Back & arms (limited)", "Maintenance (annual)",
        ],
        "session_minutes": "30-45",
        "downtime": "Pigment 'coffee-grounds' for 5-7 days then flakes off; redness same-day",
        "results_timing": "Most patients see clear improvement after 3 sessions spaced 3-4 weeks apart",
        "good_candidate": "Adults with sun damage, redness, or rosacea on fair-to-medium skin tones",
        "faqs": [
            ("How is IPL different from a laser?",
             "IPL uses broadband light (multiple wavelengths) — it's less targeted than a laser but treats more concerns in one pass "
             "(brown + red + texture). Lasers are more precise for single concerns; IPL is the workhorse for overall tone."),
            ("How many IPL sessions do I need?",
             "Most patients see meaningful improvement after a series of 3 sessions spaced 3-4 weeks apart, with maintenance once a year."),
            ("Can IPL treat melasma?",
             "IPL can worsen melasma in some patients. We screen carefully and may recommend chemical peels or topical protocols instead for true melasma. "
             "For sun damage and freckles, IPL is excellent."),
        ],
    },
    # ---- SECONDARY / LONGER TAIL (top-5 cities each) ----
    {
        "slug": "dermal-filler", "tier": "secondary",
        "name": "Dermal Filler", "h1_phrase": "Dermal Fillers in {city}, CA",
        "title_label": "Dermal Filler",
        "category": "Injectables", "internal_link": "injectables.html",
        "short": "restore volume and contour the face with hyaluronic acid fillers",
        "intro": (
            "Dermal fillers (Juvederm, Restylane, RHA) use cross-linked hyaluronic acid to restore "
            "volume, sculpt cheeks and jawline, refine lips, and soften static lines that don't "
            "respond to Botox alone. Done well, filler is undetectable — it's the structural balance "
            "that catches the eye."
        ),
        "areas": [
            "Lips (subtle plump or full augmentation)", "Cheeks (midface support)",
            "Tear troughs (under-eye hollows)", "Chin & jawline (definition)",
            "Nasolabial folds (smile lines)", "Marionette lines",
            "Temple hollows", "Hands (volume restoration)",
        ],
        "session_minutes": "30-60",
        "downtime": "Mild swelling and possible bruising 24-72 hours; back to social events at day 3-5",
        "results_timing": "Immediate results that settle at 2 weeks; last 6-18 months depending on product and area",
        "good_candidate": "Adults wanting volume restoration or facial contouring without surgery",
        "faqs": [
            ("How long does dermal filler last?",
             "Most hyaluronic acid fillers last 6-18 months depending on the product, the area treated, and your metabolism. "
             "Lips and high-movement areas turn over faster; cheeks and chin last longest."),
            ("Will I look 'overdone'?",
             "Not with our injectors — we use a structural approach (cheeks and chin before lips) and conservative dosing to keep results natural. "
             "We'd rather have you come back for more than overdo it."),
            ("What's the difference between Juvederm, Restylane, and RHA?",
             "All are hyaluronic-acid fillers but with different cross-linking technologies, lift, and feel. We carry the full Allergan and Galderma "
             "lines and select based on the area and your goals — not what we have on the shelf."),
        ],
    },
    {
        "slug": "iv-therapy", "tier": "secondary",
        "name": "IV Therapy", "h1_phrase": "IV Therapy in {city}, CA",
        "title_label": "IV Therapy",
        "category": "Wellness", "internal_link": "iv-therapy.html",
        "short": "vitamin, hydration, and recovery IV drips for energy and immunity",
        "intro": (
            "Our IV therapy menu delivers vitamins, electrolytes, antioxidants, and amino acids "
            "directly into the bloodstream for faster onset than oral supplements. Popular drips "
            "include the Myers' cocktail (energy), NAD+ (longevity), Glutathione (skin glow), and "
            "Hangover Recovery."
        ),
        "areas": [
            "Myers' cocktail (immunity + energy)", "NAD+ (cellular + cognitive)",
            "Glutathione (skin + detox)", "Hydration + electrolytes",
            "Hangover recovery", "Athletic recovery (BCAA + amino)",
            "Beauty drip (biotin + B vitamins)", "Immunity boost (high-dose vitamin C)",
        ],
        "session_minutes": "30-60",
        "downtime": "None — back to normal activity immediately",
        "results_timing": "Most patients feel improved energy within hours; effects last days to weeks depending on drip",
        "good_candidate": "Adults wanting fast nutrient absorption — pre-event, post-illness, or for ongoing wellness",
        "faqs": [
            ("Does IV therapy actually work?",
             "For specific clinical scenarios — dehydration, malabsorption, certain deficiencies — yes, IV delivery is more efficient than oral. "
             "For general wellness, many patients report subjective benefits (energy, recovery, mood). We're transparent about what the evidence supports."),
            ("How often should I get IV therapy?",
             "Most patients do once-monthly maintenance or pre-event boosts. Athletes and frequent travelers sometimes do weekly. We help you build "
             "a cadence that fits your goals and budget."),
            ("Is IV therapy safe?",
             "IVs are placed by licensed RNs in a clinical setting. We screen for contraindications, monitor during the drip, and use only "
             "pharmaceutical-grade ingredients."),
        ],
    },
    {
        "slug": "hydrafacial", "tier": "secondary",
        "name": "HydraFacial", "h1_phrase": "HydraFacial in {city}, CA",
        "title_label": "HydraFacial",
        "category": "Skin & Laser", "internal_link": "skin-laser.html",
        "short": "deep-cleanse, exfoliate, and hydrate skin in one 30-minute treatment",
        "intro": (
            "HydraFacial is a multi-step facial that cleanses, exfoliates, extracts, and hydrates "
            "skin using patented vortex technology. It's a zero-downtime treatment ideal as a monthly "
            "maintenance facial or a pre-event glow-up."
        ),
        "areas": [
            "Full face deep cleanse", "Comedone extractions",
            "Anti-aging boosters", "Brightening boosters",
            "Acne-prone skin", "Sensitive skin protocol",
            "Lymphatic drainage add-on", "LED light therapy add-on",
        ],
        "session_minutes": "30-45",
        "downtime": "None — makeup-ready same day",
        "results_timing": "Immediate glow; benefits build with monthly treatments",
        "good_candidate": "All skin types wanting a non-irritating, customizable medical-grade facial",
        "faqs": [
            ("How often should I get a HydraFacial?",
             "Monthly is the sweet spot — it aligns with your skin's natural turnover cycle. Brides and event-goers often book a series of 3 in "
             "the weeks before."),
            ("HydraFacial vs. regular facial — what's the difference?",
             "A standard facial is largely manual (steaming, hands-on extractions). HydraFacial uses a patented vortex tip that suctions debris while "
             "infusing serums — it's gentler, faster, and more consistent than manual extractions."),
            ("Can I get HydraFacial with sensitive skin or rosacea?",
             "Yes — we customize boosters and pressure to skin type. Many rosacea patients tolerate HydraFacial well when stronger treatments aren't safe."),
        ],
    },
    {
        "slug": "chemical-peel", "tier": "secondary",
        "name": "Chemical Peel", "h1_phrase": "Chemical Peels in {city}, CA",
        "title_label": "Chemical Peels",
        "category": "Skin & Laser", "internal_link": "skin-laser.html",
        "short": "smooth texture and brighten tone with medical-grade chemical exfoliation",
        "intro": (
            "Medical-grade chemical peels use controlled acid solutions to exfoliate damaged surface "
            "skin and stimulate new collagen. We offer light, medium, and depth-customized peels to "
            "match your skin type, goals, and downtime tolerance."
        ),
        "areas": [
            "Glycolic peel (radiance)", "Salicylic peel (acne)",
            "Lactic peel (sensitive skin)", "TCA peel (medium depth)",
            "Jessner peel (pigmentation)", "VI Peel (full-face brightening)",
            "Back peel (bacne)", "Chest & décolletage (sun damage)",
        ],
        "session_minutes": "30-60",
        "downtime": "Light peels: none-1 day. Medium peels: 3-7 days of peeling.",
        "results_timing": "Light peels: glow at 1-2 days. Medium peels: brightened, smoother skin at day 7-10. Series of 3-6 recommended.",
        "good_candidate": "Adults targeting texture, dullness, mild scarring, or pigmentation",
        "faqs": [
            ("Which chemical peel is right for me?",
             "Lighter peels (lactic, salicylic) are good monthly maintenance with no downtime. Medium peels (TCA, Jessner) deliver stronger results "
             "but require 3-7 days of healing. We choose based on your skin type and how much downtime you can take."),
            ("How often can I get a chemical peel?",
             "Light peels can be done every 2-4 weeks. Medium peels are typically spaced 6-12 weeks apart. We build series tailored to your goals."),
            ("Will my skin peel visibly?",
             "Light peels usually cause subtle flaking by day 2-3. Medium peels produce visible peeling for 3-7 days — you can predict downtime "
             "based on the depth we choose."),
        ],
    },
]

CITIES = [
    {
        "slug": "carlsbad", "name": "Carlsbad", "zip": "92008",
        "drive_min": 12, "drive_distance": "9 miles",
        "neighborhoods": ["Carlsbad Village", "La Costa", "Aviara", "Bressi Ranch"],
        "landmark": "Carlsbad Village",
        "from_route": "Take I-5 South to Palomar Airport Road, head east, right on Melrose Drive, continue to Vale Terrace Drive.",
        "local_hook": "Carlsbad residents — including many who commute from Bressi Ranch and Aviara — choose us over La Jolla clinics for shorter drive time and free parking.",
    },
    {
        "slug": "encinitas", "name": "Encinitas", "zip": "92024",
        "drive_min": 22, "drive_distance": "17 miles",
        "neighborhoods": ["Olivenhain", "Cardiff", "Leucadia", "Old Encinitas"],
        "landmark": "Moonlight Beach",
        "from_route": "Take I-5 North to CA-78 East, exit Melrose Drive, north to Vale Terrace Drive.",
        "local_hook": "Encinitas patients — especially those in Olivenhain and the coastal Cardiff stretch — appreciate our small-clinic feel and same-week booking versus the long waits at coastal aesthetic chains.",
    },
    {
        "slug": "san-marcos", "name": "San Marcos", "zip": "92078",
        "drive_min": 11, "drive_distance": "7 miles",
        "neighborhoods": ["San Elijo Hills", "Lake San Marcos", "Old San Marcos", "Twin Oaks Valley"],
        "landmark": "Cal State San Marcos",
        "from_route": "Take CA-78 West to Sycamore Drive exit, north to Vista, west to Vale Terrace Drive.",
        "local_hook": "San Marcos patients (from San Elijo Hills, Lake San Marcos, and the CSUSM area) are some of our most frequent visitors — we're a quick ride down the 78.",
    },
    {
        "slug": "escondido", "name": "Escondido", "zip": "92025",
        "drive_min": 18, "drive_distance": "14 miles",
        "neighborhoods": ["Old Escondido", "Hidden Meadows", "South Escondido", "North County"],
        "landmark": "Westfield North County",
        "from_route": "Take CA-78 West toward Vista, exit Sycamore, continue to Vale Terrace Drive.",
        "local_hook": "Escondido residents save a trip into downtown San Diego — we offer the same medical-grade lasers and injectables 18 minutes west.",
    },
    {
        "slug": "oceanside", "name": "Oceanside", "zip": "92054",
        "drive_min": 14, "drive_distance": "10 miles",
        "neighborhoods": ["South Oceanside", "Fire Mountain", "Rancho Del Oro", "Downtown Oceanside"],
        "landmark": "Oceanside Pier",
        "from_route": "Take CA-76 East to College Boulevard, south to Vista Way, east to Vale Terrace Drive.",
        "local_hook": "Oceanside patients — including many military families from Camp Pendleton — choose us for natural-looking injectables and discreet, professional care.",
    },
    {
        "slug": "vista", "name": "Vista", "zip": "92084",
        "drive_min": 0, "drive_distance": "in-town",
        "neighborhoods": ["Shadowridge", "Vista Village", "Buena Vista", "Foothill"],
        "landmark": "Vista Village",
        "from_route": "We're located at 969 Vale Terrace Drive, Suite B — central Vista, easy access from Melrose, Vista Way, and 78.",
        "local_hook": "We're your hometown medical spa — most Vista patients drive 5-10 minutes door to door.",
    },
    {
        "slug": "solana-beach", "name": "Solana Beach", "zip": "92075",
        "drive_min": 25, "drive_distance": "19 miles",
        "neighborhoods": ["Cedros Design District", "Eden Gardens", "Lomas Santa Fe"],
        "landmark": "Cedros Design District",
        "from_route": "Take I-5 North to CA-78 East, exit Melrose Drive, head north to Vale Terrace Drive.",
        "local_hook": "Solana Beach patients drive up for our medical-spa pricing and concierge-style scheduling — without the parking headaches of the coastal corridor.",
    },
    {
        "slug": "del-mar", "name": "Del Mar", "zip": "92014",
        "drive_min": 28, "drive_distance": "22 miles",
        "neighborhoods": ["Del Mar Village", "Del Mar Heights", "Carmel Valley"],
        "landmark": "Del Mar Racetrack",
        "from_route": "Take I-5 North to CA-78 East, exit Melrose Drive, head north to Vale Terrace Drive.",
        "local_hook": "Del Mar patients — especially those in Carmel Valley and Del Mar Heights — choose us for board-certified results without coastal-corridor pricing.",
    },
    {
        "slug": "rancho-bernardo", "name": "Rancho Bernardo", "zip": "92128",
        "drive_min": 30, "drive_distance": "23 miles",
        "neighborhoods": ["Westwood", "Oaks North", "Bernardo Heights", "Carmel Mountain"],
        "landmark": "Bernardo Winery",
        "from_route": "Take I-15 North to CA-78 West, exit Sycamore Avenue, continue to Vale Terrace Drive.",
        "local_hook": "Rancho Bernardo patients prefer our smaller-clinic personal attention over the larger Scripps and 4S Ranch chains.",
    },
    {
        "slug": "poway", "name": "Poway", "zip": "92064",
        "drive_min": 32, "drive_distance": "24 miles",
        "neighborhoods": ["Old Poway", "Green Valley", "Garden Road", "Sycamore Estates"],
        "landmark": "Lake Poway",
        "from_route": "Take I-15 North to CA-78 West, exit Sycamore Avenue, continue to Vale Terrace Drive.",
        "local_hook": "Poway patients tell us our small-town feel reminds them of home — and we run on time so the drive is worth it.",
    },
]


def html_escape(s: str) -> str:
    return html.escape(s, quote=True)


def render_page(service: dict, city: dict) -> str:
    s_slug = service["slug"]
    c_slug = city["slug"]
    slug = f"{s_slug}-{c_slug}-ca"
    url_canonical = f"https://transformativemedspa.com/{slug}"

    title = f"{service['title_label']} in {city['name']}, CA | Transformative Wellness"
    meta_desc = (
        f"{service['name']} for {city['name']} residents at Transformative Wellness — "
        f"{city['drive_distance']} from {city['name']} ({city['drive_min']}-min drive). "
        f"Board-certified care. $50 consultations, credited toward treatment. Call {PHONE}."
    )
    h1 = service["h1_phrase"].format(city=city["name"])

    areas_html = "\n".join(
        f'                        <li><i class="fas fa-check" style="color: var(--color-sage); margin-right: var(--spacing-xs);"></i>{html_escape(a)}</li>'
        for a in service["areas"]
    )

    faqs_html = "\n".join(
        f"""                <details class="faq-item" style="background:#fff; border:1px solid var(--color-cream); border-radius: var(--radius-md); padding: var(--spacing-md); margin-bottom: var(--spacing-sm);">
                    <summary style="cursor:pointer; font-weight:600;">{html_escape(q)}</summary>
                    <p style="margin-top: var(--spacing-sm); margin-bottom:0;">{html_escape(a)}</p>
                </details>"""
        for q, a in service["faqs"]
    )

    related_cities = [c for c in CITIES if c["slug"] != c_slug][:5]
    related_cities_html = "\n".join(
        f'                        <li><a href="{s_slug}-{c["slug"]}-ca.html">{html_escape(service["name"])} in {html_escape(c["name"])}</a></li>'
        for c in related_cities
    )
    related_services = [s for s in SERVICES if s["slug"] != s_slug and s["tier"] == "core"][:5]
    related_services_html = "\n".join(
        f'                        <li><a href="{s["slug"]}-{c_slug}-ca.html">{html_escape(s["name"])} in {html_escape(city["name"])}</a></li>'
        for s in related_services
    )

    if city["drive_min"] == 0:
        proximity_line = f"Our flagship Vista location at {ADDR_STREET}."
    else:
        proximity_line = f"About {city['drive_distance']} ({city['drive_min']} minutes) from {city['name']} to our Vista location."

    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalBusiness",
        "name": f"Transformative Wellness — {service['name']} for {city['name']}",
        "description": meta_desc,
        "url": url_canonical,
        "telephone": PHONE_E164,
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ADDR_STREET,
            "addressLocality": ADDR_CITY,
            "addressRegion": "CA",
            "postalCode": ADDR_ZIP,
            "addressCountry": "US",
        },
        "areaServed": {"@type": "City", "name": city["name"], "containedIn": "California"},
        "makesOffer": {
            "@type": "Offer",
            "itemOffered": {
                "@type": "MedicalProcedure",
                "name": service["name"],
                "description": service["intro"],
            },
        },
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in service["faqs"]
        ],
    }

    neighborhoods_inline = ", ".join(city["neighborhoods"][:3])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html_escape(title)}</title>
    <meta name="description" content="{html_escape(meta_desc)}">
    <link rel="canonical" href="{url_canonical}">

    <script type="application/ld+json">
{json.dumps(schema, indent=4)}
    </script>
    <script type="application/ld+json">
{json.dumps(faq_schema, indent=4)}
    </script>

    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/ageless.css">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Serif+Text:ital@0;1&family=Inter:wght@300;400;500;600&family=Montserrat:wght@500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <meta property="og:title" content="{html_escape(title)}">
    <meta property="og:description" content="{html_escape(meta_desc)}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{url_canonical}">
    <meta property="og:image" content="https://transformativemedspa.com/images/lobby/lobby-reception-new.jpg">
    <meta property="og:site_name" content="Transformative Wellness">
    <meta property="og:locale" content="en_US">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html_escape(title)}">
    <meta name="twitter:description" content="{html_escape(meta_desc)}">
    <meta name="twitter:image" content="https://transformativemedspa.com/images/lobby/lobby-reception-new.jpg">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="images/logo.png" alt="Transformative Wellness" class="logo-img">
            </a>
            <ul class="nav-menu">
                <li><a href="services.html">Services</a></li>
                <li><a href="concerns.html">Concerns</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="https://ageless.ai/a/transformativewellness/transformation" class="nav-ageless-link" target="_blank" rel="noopener noreferrer">AI Treatment Advisor<span class="nav-ageless-new" aria-hidden="true">NEW</span></a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
            <a href="{BOOK_URL}" class="btn btn-primary nav-cta">Book online</a>
        </div>
    </nav>

    <section class="page-header">
        <div class="container">
            <span class="section-label">Serving {html_escape(city["name"])}, CA</span>
            <h1>{html_escape(h1)}</h1>
            <p>{html_escape(proximity_line)} {html_escape(service["short"].capitalize())}.</p>
        </div>
    </section>

    <section style="padding: var(--spacing-3xl) 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--spacing-3xl); align-items: start;">
                <div>
                    <h2>{html_escape(service["name"])} for {html_escape(city["name"])} Patients</h2>
                    <p>{html_escape(service["intro"])}</p>
                    <p>{html_escape(city["local_hook"])}</p>
                    <h3 style="margin-top: var(--spacing-lg);">What we treat</h3>
                    <ul style="list-style: none; margin: 0 0 var(--spacing-lg) 0; padding: 0;">
{areas_html}
                    </ul>
                </div>
                <aside style="background: var(--color-cream); padding: var(--spacing-xl); border-radius: var(--radius-lg);">
                    <h3>Treatment at a glance</h3>
                    <dl style="margin: 0;">
                        <dt style="font-weight: 600; margin-top: var(--spacing-sm);">Session length</dt>
                        <dd style="margin: 0 0 var(--spacing-xs) 0;">{html_escape(service["session_minutes"])} minutes</dd>
                        <dt style="font-weight: 600; margin-top: var(--spacing-sm);">Downtime</dt>
                        <dd style="margin: 0 0 var(--spacing-xs) 0;">{html_escape(service["downtime"])}</dd>
                        <dt style="font-weight: 600; margin-top: var(--spacing-sm);">Results</dt>
                        <dd style="margin: 0 0 var(--spacing-xs) 0;">{html_escape(service["results_timing"])}</dd>
                        <dt style="font-weight: 600; margin-top: var(--spacing-sm);">Good candidate</dt>
                        <dd style="margin: 0;">{html_escape(service["good_candidate"])}</dd>
                    </dl>
                    <a href="{BOOK_URL}" class="btn btn-primary" style="display: block; text-align: center; margin-top: var(--spacing-lg);">Book Consultation</a>
                </aside>
            </div>
        </div>
    </section>

    <section style="padding: var(--spacing-3xl) 0; background: var(--color-cream);">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--spacing-3xl); align-items: center;">
                <div>
                    <h2>Easy Drive from {html_escape(city["name"])}</h2>
                    <p><strong>{html_escape(proximity_line)}</strong></p>
                    <p>Most {html_escape(city["name"])} patients arrive from {html_escape(neighborhoods_inline)}. {html_escape(city["from_route"])}</p>
                    <p>Free parking, no valet, no traffic — most appointments take less time than the drive in.</p>
                </div>
                <div>
                    <h3>Why {html_escape(city["name"])} patients choose us</h3>
                    <ul style="list-style: none; margin: 0;">
                        <li style="margin-bottom: var(--spacing-sm);"><i class="fas fa-check" style="color: var(--color-sage); margin-right: var(--spacing-xs);"></i>Board-certified medical director (Dr. Joshua Yang)</li>
                        <li style="margin-bottom: var(--spacing-sm);"><i class="fas fa-check" style="color: var(--color-sage); margin-right: var(--spacing-xs);"></i>4.9★ across 150+ Google reviews</li>
                        <li style="margin-bottom: var(--spacing-sm);"><i class="fas fa-check" style="color: var(--color-sage); margin-right: var(--spacing-xs);"></i>Cherry, CareCredit, and Affirm financing</li>
                        <li style="margin-bottom: var(--spacing-sm);"><i class="fas fa-check" style="color: var(--color-sage); margin-right: var(--spacing-xs);"></i>Free parking and no valet</li>
                        <li style="margin-bottom: var(--spacing-sm);"><i class="fas fa-check" style="color: var(--color-sage); margin-right: var(--spacing-xs);"></i>Beauty Bank &amp; Perks membership savings</li>
                        <li><i class="fas fa-check" style="color: var(--color-sage); margin-right: var(--spacing-xs);"></i>Same-week booking on most services</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section style="padding: var(--spacing-3xl) 0;">
        <div class="container" style="max-width: 820px;">
            <h2 style="text-align: center; margin-bottom: var(--spacing-xl);">{html_escape(service["name"])} FAQs — {html_escape(city["name"])} patients ask</h2>
{faqs_html}
        </div>
    </section>

    <section style="padding: var(--spacing-2xl) 0; background: var(--color-cream);">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--spacing-3xl);">
                <div>
                    <h3>Other services for {html_escape(city["name"])} patients</h3>
                    <ul style="list-style: none; margin: 0; padding: 0;">
{related_services_html}
                    </ul>
                </div>
                <div>
                    <h3>{html_escape(service["name"])} for nearby cities</h3>
                    <ul style="list-style: none; margin: 0; padding: 0;">
{related_cities_html}
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <div class="cta-content">
                <h2>Ready to book {html_escape(service["name"])} from {html_escape(city["name"])}?</h2>
                <p>$50 consultations, credited toward treatment. Same-week appointments. Talk to a real provider before you commit.</p>
                <div class="cta-buttons">
                    <a href="{BOOK_URL}" class="btn btn-primary btn-large">Book Consultation</a>
                    <a href="tel:{PHONE_E164}" class="btn btn-outline btn-large"><i class="fas fa-phone"></i> {PHONE}</a>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer footer-premium">
        <div class="container">
            <div class="footer-grid-premium">
                <div class="footer-brand">
                    <a href="index.html" class="footer-logo">
                        <span class="logo-script">Transformative</span>
                        <span class="logo-main">Wellness</span>
                    </a>
                    <p class="footer-tagline">Vista&apos;s Premier Medical Spa — natural injectables, laser, weight care &amp; IV therapy.</p>
                </div>
                <div class="footer-links">
                    <h4>Quick links</h4>
                    <ul>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="before-after.html">Results</a></li>
                        <li><a href="memberships.html">Memberships</a></li>
                        <li><a href="about.html">About</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Top treatments</h4>
                    <ul>
                        <li><a href="injectables.html">Botox &amp; Fillers</a></li>
                        <li><a href="skin-laser.html">Laser &amp; Skin</a></li>
                        <li><a href="body-weight.html">Weight Loss</a></li>
                        <li><a href="iv-therapy.html">IV therapy</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Visit &amp; hours</h4>
                    <p><i class="fas fa-map-marker-alt"></i> {ADDR_STREET}<br>{ADDR_CITY}, CA {ADDR_ZIP}</p>
                    <p><i class="fas fa-phone"></i> <a href="tel:{PHONE_E164}">{PHONE}</a></p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Transformative Wellness. All rights reserved.</p>
                <div class="footer-legal">
                    <a href="privacy-policy.html">Privacy</a>
                    <a href="terms-of-service.html">Terms</a>
                    <a href="medical-disclaimer.html">HIPAA</a>
                    <a href="accessibility.html">Accessibility</a>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
"""


def main():
    pages = []
    for service in SERVICES:
        cities_for_service = CITIES if service["tier"] == "core" else [c for c in CITIES if c["slug"] in TOP_CITY_SLUGS]
        for city in cities_for_service:
            slug = f"{service['slug']}-{city['slug']}-ca"
            path = OUT_DIR / f"{slug}.html"
            html_out = render_page(service, city)
            path.write_text(html_out)
            pages.append((slug, len(html_out)))

    sitemap_lines = [
        f"    <url><loc>https://transformativemedspa.com/{slug}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>"
        for slug, _ in pages
    ]
    SITEMAP_FRAGMENT.write_text("\n".join(sitemap_lines) + "\n")

    core_count = sum(1 for s in SERVICES if s["tier"] == "core") * len(CITIES)
    sec_count = sum(1 for s in SERVICES if s["tier"] == "secondary") * len(TOP_CITY_SLUGS)
    print(f"Generated {len(pages)} pages (core {core_count} + secondary {sec_count}).")
    print(f"Sitemap fragment: {SITEMAP_FRAGMENT}")
    print(f"Sample sizes (first 3): {pages[:3]}")
    print(f"Total bytes: {sum(b for _, b in pages):,}")


if __name__ == "__main__":
    main()
