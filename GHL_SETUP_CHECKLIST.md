# GHL Chatbot Setup Checklist

## ✅ STEP 1: Access GHL Dashboard
- [ ] Go to https://app.gohighlevel.com
- [ ] Log into your account
- [ ] Verify you're in the correct location (Transformative Wellness)

---

## ✅ STEP 2: Configure Chat Widget Settings

**Path:** Settings → Chat Widget

### Widget Appearance
- [ ] Enable "Webchat Widget"
- [ ] Primary Color: `#5c4135` (Deep Cocoa — matches website chat embed)
- [ ] Secondary Color: `#9ac1c4` (Ocean Mist — matches website accent)
- [ ] Widget Position: Bottom Right
- [ ] Show Avatar: YES
- [ ] Upload avatar image (logo or team photo)

### Widget Text
- [ ] Welcome Message: `Hi there! 👋 How can we help you today?`
- [ ] Team Name: `Transformative Wellness`
- [ ] Sub-heading: `We typically reply within minutes`
- [ ] Pre-chat Message: (optional)

### Business Hours
- [ ] Monday: 9:00 AM - 6:00 PM
- [ ] Tuesday: CLOSED
- [ ] Wednesday: 9:00 AM - 6:00 PM
- [ ] Thursday: CLOSED
- [ ] Friday: 9:00 AM - 6:00 PM
- [ ] Saturday: 9:00 AM - 4:00 PM
- [ ] Sunday: Closed
- [ ] Timezone: America/Los_Angeles (Pacific Time)

### Offline Message
- [ ] Set auto-reply for after-hours:
```
Hi! 👋 Thanks for reaching out to Transformative Wellness.

Our office is currently closed. Our hours are:
Monday: 9am - 6pm
Tuesday: CLOSED
Wednesday: 9am - 6pm
Thursday: CLOSED
Friday: 9am - 6pm
Saturday: 9am - 4pm
Sunday: CLOSED

Leave your message here and we'll respond first thing when we're back! 

For immediate booking, visit: https://www.mypatientvisit.com/onlinescheduling/#/scheduler/schedule?practiceid=e47fce2c-cb7d-4f15-9af0-ff7c5ea03744
```

---

## ✅ STEP 3: Create Chatbot Flows

**Path:** Marketing → Chatbot Flows → Create New Flow

### Flow 1: Welcome Menu (Default Flow)
- [ ] Create flow named "Welcome Menu"
- [ ] Set as default/start flow
- [ ] Add welcome message from GHL_CHATBOT_SETUP.md
- [ ] Add 5 quick reply buttons:
  1. 🗓️ Book Consultation ($25, applied to treatment)
  2. 💉 Treatment Info
  3. 💰 Pricing & Packages
  4. 📍 Location & Hours
  5. 💬 Speak to Someone

### Flow 2: Book Consultation
- [ ] Create flow named "Book Consultation"
- [ ] Add message with booking options
- [ ] Add 3 quick reply buttons:
  1. 📅 Book Online Now → Action: Open URL
  2. 📞 Call (858) 444-0414 → Action: Call Number
  3. 💬 Text Us → Action: Request input

### Flow 3: Treatment Info
- [ ] Create flow named "Treatment Info"
- [ ] Add message listing services
- [ ] Add 6 quick reply buttons:
  1. 💉 Injectables
  2. ✨ Skin & Laser
  3. ⚖️ Medical Weight Loss
  4. 💧 IV Therapy
  5. 👁️ Lashes & Hair Removal
  6. 🤔 Not Sure - Help Me Choose

### Flow 4: Pricing & Packages
- [ ] Create flow named "Pricing"
- [ ] Add pricing overview message
- [ ] Add 3 quick reply buttons:
  1. Get Custom Quote
  2. View Membership Details
  3. Current Promotions

### Flow 5: Location & Hours
- [ ] Create flow named "Location"
- [ ] Add address and hours
- [ ] Add 3 quick reply buttons:
  1. Get Directions → Action: Open Google Maps
  2. Book Appointment
  3. Contact Us

### Flow 6: Speak to Human
- [ ] Create flow named "Speak to Human"
- [ ] Add contact info message (include BOTH phone numbers: 858-444-0414 for Vista, 951-446-6623 for UFC locations)
- [ ] Set action: "Transfer to Live Chat" or "Notify Team"
- [ ] Add 3 quick reply buttons:
  1. Call Vista: 858-444-0414
  2. Call UFC Locations: 951-446-6623
  3. Book Online

---

## ✅ STEP 4: Create Sub-Flows (Treatment Details)

### Flow 3A: Injectables
- [ ] Create flow with Botox, Filler, Kybella info
- [ ] Add pricing
- [ ] Add FAQ
- [ ] Add "Book Consultation" button

### Flow 3B: Skin & Laser
- [ ] Create flow listing all laser treatments
- [ ] Add ClearLift, CO2 CoolPeel, IPL, Microneedling
- [ ] Add pricing for each
- [ ] Add "Book Free Skin Consultation" button

### Flow 3C: Medical Weight Loss
- [ ] Create flow about GLP-1 medications
- [ ] Add Semaglutide/Tirzepatide info
- [ ] Add pricing ($400-600/month)
- [ ] Add "Schedule Weight Loss Consult" button

### Flow 3D: IV Therapy
- [ ] Create flow listing IV options
- [ ] Add Hydration, Energy, Immunity, NAD+ pricing
- [ ] Add "Book IV Therapy" button

### Flow 3E: Lashes & Smooth
- [ ] Create flow with lash lift, brow lamination, laser hair removal
- [ ] Add pricing
- [ ] Add "Book Service" button

### Flow 7: Memberships (NEW)
- [ ] Create flow named "Memberships"
- [ ] Add Beauty Bank ($149/month) and Perks ($49/month) details
- [ ] Include benefits: monthly credits, neurotoxin discounts, GLP-1 discounts
- [ ] Add 3 quick reply buttons:
  1. Join Beauty Bank
  2. Join Perks
  3. Schedule Consultation

### Flow 8: Financing (NEW)
- [ ] Create flow named "Financing"
- [ ] Add financing options: Cherry, CareCredit, Affirm
- [ ] Mention membership savings
- [ ] Add 3 quick reply buttons:
  1. Schedule Consultation
  2. Learn About Memberships
  3. Apply for Financing

### Flow 9: Consultation Fee (NEW)
- [ ] Create flow named "Consultation Fee"
- [ ] Explain $25 fee (applied toward treatment)
- [ ] List what's included: assessment, goal review, Signature Transformation plan
- [ ] Add 3 quick reply buttons:
  1. Schedule Consultation
  2. Learn About Services
  3. Contact Us

---

## ✅ STEP 5: Set Up Keyword Triggers

**Path:** Marketing → Chatbot Flows → Keywords

| Keyword | Action |
|---------|--------|
| `price`, `cost`, `how much` | → Send to Flow 4: Pricing |
| `book`, `appointment`, `schedule` | → Send to Flow 2: Book Consultation |
| `botox`, `filler`, `injectable`, `dysport` | → Send to Flow 3A: Injectables |
| `laser`, `facial`, `skin`, `clearlift`, `co2`, `ipl` | → Send to Flow 3B: Skin & Laser |
| `weight`, `semaglutide`, `tirzepatide`, `ozempic`, `mounjaro` | → Send to Flow 3C: Weight Loss |
| `IV`, `drip`, `NAD`, `vitamin`, `hydration` | → Send to Flow 3D: IV Therapy |
| `hours`, `location`, `address`, `parking`, `directions` | → Send to Flow 5: Location |
| `membership`, `beauty bank`, `perks`, `package` | → Send to Flow 7: Memberships |
| `financing`, `payment plan`, `affirm`, `cherry`, `carecredit` | → Send to Flow 8: Financing |
| `consultation fee`, `consultation cost`, `consultation price` | → Send to Flow 9: Consultation Fee |
| `ufc`, `murrieta`, `corona` | → Send UFC location info |
| `human`, `person`, `speak`, `call`, `phone` | → Send to Flow 6: Speak to Human |
| `complaint`, `problem`, `unhappy`, `refund`, `issue` | → Transfer to human IMMEDIATELY |

---

## ✅ STEP 6: Add Team Members

**Path:** Settings → Team Management

- [ ] Add all team members who should receive chats:
  - McKenzie (Lead RN)
  - Other RNs
  - Front desk staff
  - Office manager

- [ ] Set notification preferences:
  - [ ] Email notifications: ON
  - [ ] SMS notifications: (optional)
  - [ ] In-app notifications: ON

- [ ] Set routing rules:
  - [ ] Option 1: Round-robin (distributes evenly)
  - [ ] Option 2: Assign to specific person
  - [ ] Option 3: All team members get notified

---

## ✅ STEP 7: Upload Training Data (Optional but Recommended)

**Path:** Settings → Conversation AI (if available)

If your GHL plan includes Conversation AI:
- [ ] Upload GHL_CHATBOT_TRAINING_DATA.md
- [ ] Or copy-paste key sections into training data
- [ ] Train AI on:
  - Services and pricing
  - Common questions and answers
  - Business information
  - Team credentials

---

## ✅ STEP 8: Test Everything

### Test Each Flow
- [ ] Open website in incognito mode
- [ ] Click chat widget
- [ ] Test welcome message appears
- [ ] Click each button and verify correct flow
- [ ] Test keyword triggers (type "price", "botox", etc.)

### Test After Hours
- [ ] Change computer time to Sunday 10 PM
- [ ] Open chat widget
- [ ] Verify offline message appears

### Test Mobile
- [ ] Open website on phone
- [ ] Test chat widget on mobile
- [ ] Verify quick replies work

### Test Escalation
- [ ] Type "speak to human"
- [ ] Verify transfer works
- [ ] Check that team gets notification

---

## ✅ STEP 9: Connect Forms (Already Done - Verify)

**Path:** Forms → Check Submissions

- [ ] Verify contact form submissions appear in GHL Contacts
- [ ] Test the form:
  1. Go to https://transformativemedspa.com/contact.html
  2. Fill out and submit form
  3. Check GHL Contacts for new entry
  4. Verify all fields captured correctly

**Webhook URL (already configured):**
```
https://api.leadconnectorhq.com/hooks/pit-2294e821-a3c5-4986-a4c9-92db5d3b5454
```

---

## ✅ STEP 10: Set Up Notifications

**Path:** Settings → Notifications

- [ ] New chat notification: ON
- [ ] New form submission: ON
- [ ] Missed chat notification: ON
- [ ] Assign notification recipients

---

## ✅ FINAL TESTING CHECKLIST

| Test | Result |
|------|--------|
| Chat widget appears on homepage | ⬜ Pass ⬜ Fail |
| Welcome message displays correctly | ⬜ Pass ⬜ Fail |
| Quick reply buttons work | ⬜ Pass ⬜ Fail |
| Book Consultation flow works | ⬜ Pass ⬜ Fail |
| Treatment Info flow works | ⬜ Pass ⬜ Fail |
| Pricing flow works | ⬜ Pass ⬜ Fail |
| Location flow works | ⬜ Pass ⬜ Fail |
| Speak to Human transfers correctly | ⬜ Pass ⬜ Fail |
| Keyword triggers work | ⬜ Pass ⬜ Fail |
| After-hours message works | ⬜ Pass ⬜ Fail |
| Contact form submits to GHL | ⬜ Pass ⬜ Fail |
| Mobile experience works | ⬜ Pass ⬜ Fail |
| Team receives notifications | ⬜ Pass ⬜ Fail |

---

## 🆘 TROUBLESHOOTING

### Widget Not Appearing
- Check if widget is enabled in GHL Settings
- Verify location ID matches: `tk_5d18d5afd6104cd28cf7658e6aba2307`
- Clear browser cache
- Check browser console for errors

### Flows Not Working
- Verify flows are published (not in draft)
- Check that flows are connected to buttons
- Test each flow individually in GHL

### Form Not Submitting
- Verify webhook URL is correct
- Check form fields match GHL field names
- Test with simple submission first

### Not Getting Notifications
- Check notification settings in GHL
- Verify email addresses are correct
- Check spam/junk folders

---

## 📞 SUPPORT RESOURCES

**GHL Help Center:** https://help.gohighlevel.com  
**GHL YouTube:** Search "HighLevel chat widget setup"  
**GHL Support Chat:** Available in your dashboard  

**Your Account Info:**
- Location ID: `tk_5d18d5afd6104cd28cf7658e6aba2307`
- Tracking ID: `tk_5d18d5afd6104cd28cf7658e6aba2307`
- Webhook: `pit-2294e821-a3c5-4986-a4c9-92db5d3b5454`

---

## ✅ COMPLETION

**Once all items are checked, your chatbot is LIVE and ready!**

Estimated setup time: 2-3 hours  
Last updated: February 2026
