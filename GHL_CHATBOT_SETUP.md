# GHL Chatbot Setup Guide for Transformative Wellness

## 🎯 Overview

Your chat widget is live on the website. Now you need to configure the conversation flows in your GHL dashboard.

**Access:** https://app.gohighlevel.com → Settings → Chat Widget

---

## ✅ Pre-Configured (Already Done)

### Website-Side Settings (in HTML code):
- Welcome message: "Hi there! 👋 How can we help you today?"
- Heading: "Transformative Wellness"
- Sub-heading: "We typically reply within minutes"
- Colors: Gold (#c9a86c) and Dark (#1a1a1a)
- Avatar: Enabled
- Location ID: tk_5d18d5afd6104cd28cf7658e6aba2307

---

## 🤖 Chat Flow Scripts

### FLOW 1: Welcome & Main Menu

**Trigger:** New visitor opens chat

**Bot Message:**
```
Hi there! 👋 Welcome to Transformative Wellness.

We're Vista's premier medical spa specializing in natural-looking results. Our board-certified team has performed 5,000+ treatments, and we're rated 4.9/5 stars by our patients.

How can we help you today?
```

**Quick Reply Buttons:**
1. 🗓️ Book Consultation (Free)
2. 💉 Treatment Info
3. 💰 Pricing & Packages
4. 📍 Location & Hours
5. 💬 Speak to Someone

---

### FLOW 2: Book Consultation

**If user clicks "Book Consultation":**

**Bot Message:**
```
Great choice! 🎉 

We offer complimentary consultations where you'll meet with one of our expert injectors. We'll discuss your goals and create a personalized treatment plan.

Choose how you'd like to book:
```

**Quick Reply Buttons:**
1. 📅 Book Online Now
2. 📞 Call (858) 444-0414
3. 💬 Text Us

**Actions:**
- Button 1 → Open: https://www.mypatientvisit.com/onlinescheduling/#/scheduler/schedule?practiceid=e47fce2c-cb7d-4f15-9af0-ff7c5ea03744
- Button 2 → Call: 8584440414
- Button 3 → Request phone number input

---

### FLOW 3: Treatment Info

**If user clicks "Treatment Info":**

**Bot Message:**
```
We offer a full range of aesthetic and wellness services! What are you most interested in?
```

**Quick Reply Buttons:**
1. 💉 Injectables (Botox, Fillers)
2. ✨ Skin & Laser Treatments
3. ⚖️ Medical Weight Loss
4. 💧 IV Therapy
5. 👁️ Lashes & Hair Removal
6. 🤔 Not Sure - Help Me Choose

---

#### FLOW 3A: Injectables

**Bot Message:**
```
Our injectable treatments include:

💉 BOTOX / DYSPORT - $12-14/unit
• Smooths forehead lines, crow's feet, frown lines
• Results last 3-4 months
• No downtime

💋 DERMAL FILLERS - $650-850/syringe
• Lip enhancement, cheek volume, under-eye hollows
• Results last 6-18 months
• Immediate results

Our injectors are board-certified nurses with specialized aesthetic training. We focus on natural-looking results - never frozen or overdone.

Want to learn more or book?
```

**Quick Reply Buttons:**
- Book Consultation
- View Before & After Photos
- Speak to an Injector

---

#### FLOW 3B: Skin & Laser

**Bot Message:**
```
Our laser and skin treatments include:

✨ CLEARLIFT "Lunchtime Laser" - $300-500
• Zero downtime, gradual improvement
• Perfect for maintenance

🔥 CO2 COOLPEEL - $800-1,200
• Dramatic results for wrinkles & sun damage
• 3-7 days social downtime

🌈 IPL PHOTOFACIAL - $350-500
• Brown spots, redness, sun damage
• Series recommended

🪡 MICRONEEDLING - $400-600
• Collagen stimulation, acne scars
• Minimal downtime

Not sure which is right for you? Book a free skin consultation!
```

**Quick Reply Buttons:**
- Book Free Skin Consultation
- Learn About Each Treatment
- Check Pricing

---

#### FLOW 3C: Medical Weight Loss

**Bot Message:**
```
Our Medical Weight Loss program uses FDA-cleared GLP-1 medications:

⚖️ SEMAGLUTIDE (Wegovy/Ozempic)
⚖️ TIRZEPATIDE (Mounjaro/Zepbound)

Program includes:
✓ Weekly injections
✓ Medical monitoring
✓ Personalized nutrition guidance
✓ Monthly follow-ups

💰 Pricing: $400-600/month (memberships save $100/month)

Most patients lose 15-20% of body weight over 12-18 months.

Ready to start your journey?
```

**Quick Reply Buttons:**
- Schedule Weight Loss Consult
- Learn About GLP-1s
- Membership Info

---

#### FLOW 3D: IV Therapy

**Bot Message:**
```
IV Vitamin Therapy delivers nutrients directly to your bloodstream:

💧 HYDRATION DRIP - $150
• Instant hydration, hangover relief

⚡ ENERGY BOOST - $175
• B12, B-complex, amino acids

🛡️ IMMUNITY DRIP - $195
• Vitamin C, zinc, glutathione

🧬 NAD+ THERAPY - $500-750
• Anti-aging, cellular repair
• The "gold standard" in wellness

Sessions take 45-60 minutes. Perfect for a mid-day wellness boost!
```

**Quick Reply Buttons:**
- Book IV Therapy
- View All IV Options
- Gift Cards Available?

---

#### FLOW 3E: Lashes & Hair Removal

**Bot Message:**
```
Enhance your natural beauty:

👁️ LASH LIFT & TINT - $125
• Natural lashes, curled & darkened
• Lasts 6-8 weeks

✨ BROW LAMINATION - $85
• Fuller, sculpted brows
• Lasts 4-6 weeks

🔴 LASER HAIR REMOVAL
• Face, body, Brazilian
• Packages available
• Series of 6-8 treatments recommended

💎 DERMAPLANING - $95
• Removes peach fuzz & dead skin
• Makeup goes on flawlessly
```

**Quick Reply Buttons:**
- Book Lash/Brow Service
- Laser Hair Removal Consult
- See All Options

---

#### FLOW 3F: Not Sure - Help Me Choose

**Bot Message:**
```
No worries! Let us help you find the perfect treatment. 

Take our quick "Find Your Treatment" quiz, or answer a few questions here:

What's your primary concern?
```

**Quick Reply Buttons:**
1. Fine lines & wrinkles
2. Acne or acne scars
3. Uneven skin tone/texture
4. Weight management
5. Low energy/fatigue
6. Unwanted hair

**Then route to appropriate flow based on selection.**

---

### FLOW 4: Pricing & Packages

**If user clicks "Pricing & Packages":**

**Bot Message:**
```
We believe in transparent pricing! Here are our most popular treatments:

💉 BOTOX - $12-14/unit
   (Most patients need 40-64 units)

💋 FILLERS - $650-850/syringe

✨ CLEARLIFT LASER - $300-500

⚖️ WEIGHT LOSS - $400-600/month

We also offer membership programs for savings:

💎 BEAUTY BANK - $149/month
• $149 monthly credit
• Discounts on all services
• Compl quarterly B12

💎 PERKS MEMBERSHIP - $49/month
• Discounts on services
• 2x yearly B12 shots

Want a personalized quote?
```

**Quick Reply Buttons:**
- Get Custom Quote
- View Membership Details
- Current Promotions

---

### FLOW 5: Location & Hours

**If user clicks "Location & Hours":**

**Bot Message:**
```
📍 Transformative Wellness
969 Vale Terrace Drive, Suite B
Vista, CA 92084

🕐 Hours:
Monday - Friday: 9am - 6pm
Saturday: 10am - 4pm
Sunday: Closed

📞 Phone: (858) 444-0414
📧 Email: info@transformativemedspa.com

We serve all of North County San Diego including Vista, Carlsbad, Oceanside, San Marcos, and Escondido.

Free parking available!
```

**Quick Reply Buttons:**
- Get Directions
- Book Appointment
- Contact Us

---

### FLOW 6: Speak to Someone

**If user clicks "Speak to Someone":**

**Bot Message:**
```
We'd love to speak with you directly!

📞 Call us: (858) 444-0414
💬 Text us: (858) 444-0414
📧 Email: info@transformativemedspa.com

During business hours, we typically answer within minutes. If you reach voicemail, leave a message and we'll call you back within 24 hours.

You can also book directly online anytime!
```

**Quick Reply Buttons:**
- Call Now
- Text Now
- Book Online

---

## 📞 Keyword Triggers (Auto-Responses)

Set up these keywords to auto-trigger responses:

| Keyword | Response |
|---------|----------|
| "price", "cost", "how much" | Send FLOW 4: Pricing |
| "book", "appointment", "schedule" | Send FLOW 2: Book Consultation |
| "botox", "filler", "injectable" | Send FLOW 3A: Injectables |
| "laser", "facial", "skin" | Send FLOW 3B: Skin & Laser |
| "weight", "semaglutide", "tirzepatide", "ozempic" | Send FLOW 3C: Weight Loss |
| "IV", "drip", "NAD" | Send FLOW 3D: IV Therapy |
| "hours", "location", "address", "parking" | Send FLOW 5: Location |
| "membership", "beauty bank", "perks" | Send membership info |
| "human", "person", "speak", "call" | Transfer to live chat or send FLOW 6 |

---

## 🕐 Business Hours Auto-Response

**During Off-Hours:**
```
Hi! 👋 Thanks for reaching out to Transformative Wellness.

Our office is currently closed. Our hours are:
Mon-Fri: 9am-6pm | Sat: 10am-4pm

Leave your message here and we'll respond first thing when we're back! 

For immediate booking, you can always schedule online at:
https://www.mypatientvisit.com/onlinescheduling/#/scheduler/schedule?practiceid=e47fce2c-cb7d-4f15-9af0-ff7c5ea03744
```

---

## 📱 GHL Setup Steps

### Step 1: Access Chat Widget Settings
1. Log into GHL: https://app.gohighlevel.com
2. Go to **Settings** (gear icon)
3. Click **Chat Widget**
4. Enable "Webchat Widget"

### Step 2: Configure Widget Appearance
- **Primary Color:** #c9a86c (gold)
- **Secondary Color:** #1a1a1a (dark)
- **Widget Position:** Bottom Right
- **Welcome Message:** "Hi there! 👋 How can we help you today?"
- **Team Name:** Transformative Wellness
- **Avatar:** Upload your logo or team photo

### Step 3: Set Business Hours
- Monday-Friday: 9:00 AM - 6:00 PM
- Saturday: 10:00 AM - 4:00 PM
- Sunday: Closed
- Timezone: America/Los_Angeles (Pacific)

### Step 4: Create Chat Flows
1. Go to **Marketing** → **Chatbot Flows**
2. Create new flow for each option above
3. Use "Quick Replies" for button options
4. Set up "If/Else" branches for different paths

### Step 5: Assign Team Members
1. Go to **Settings** → **Team Management**
2. Select who receives chat notifications
3. Set up routing rules (round-robin, assigned, etc.)

### Step 6: Test Everything
1. Open your website in incognito mode
2. Click the chat widget
3. Test every button and flow
4. Make sure booking links work
5. Verify form submissions go to GHL

---

## 🔗 Form Integration (Already Done)

Your contact form is already connected to GHL:

**Webhook:** https://api.leadconnectorhq.com/hooks/pit-2294e821-a3c5-4986-a4c9-92db5d3b5454

**Fields captured:**
- First Name
- Last Name
- Email
- Phone
- Service Interest
- Message
- Source: "Website Contact Form"
- Tracking ID: tk_5d18d5afd6104cd28cf7658e6aba2307

**Verify in GHL:**
1. Go to **Contacts**
2. Check for recent submissions
3. Test the form yourself

---

## 📊 Tracking & Analytics

**GHL External Tracking** is installed on all pages:
- Tracking ID: tk_5d18d5afd6104cd28cf7658e6aba2307

**Tracks:**
- Page views
- Form submissions
- Chat widget interactions
- Button clicks

**View in GHL:**
- Go to **Marketing** → **Stats**
- Or **Contacts** → filter by source

---

## 🆘 Need Help?

**GHL Support:**
- Help Center: https://help.gohighlevel.com
- Live Chat: Available in your GHL dashboard
- YouTube: "HighLevel Tutorials"

**Your Setup Info:**
- Location ID: tk_5d18d5afd6104cd28cf7658e6aba2307
- Domain: transformativemedspa.com
- Hosting: Cloudflare Pages
- Connected: ✅ Contact Form, ✅ Chat Widget, ✅ Tracking

---

**Last Updated:** February 2026
**Setup By:** Kimi Code AI
