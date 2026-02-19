// Treatment Quiz Logic
(function() {
    const quizForm = document.getElementById('treatmentQuiz');
    const steps = document.querySelectorAll('.quiz-step');
    const progressFill = document.getElementById('progressFill');
    const currentStepEl = document.getElementById('currentStep');
    const nextBtn = document.getElementById('nextBtn');
    const prevBtn = document.getElementById('prevBtn');
    const quizNav = document.getElementById('quizNav');
    
    let currentStep = 1;
    const totalSteps = 5;
    const formData = {};

    // Treatment recommendations database
    const recommendations = {
        wrinkles: {
            title: 'Neuromodulators (Botox/Dysport)',
            description: 'Smooth fine lines and wrinkles for a refreshed, youthful appearance.',
            treatments: [
                { name: 'The Essential', desc: '40 units - Perfect for first-timers', icon: 'fa-face-smile' },
                { name: 'The Complete', desc: '64 units - Our most popular option', icon: 'fa-star' },
                { name: 'RF Skin Tightening', desc: 'Non-invasive collagen boost', icon: 'fa-wand-magic-sparkles' }
            ],
            cta: 'Book Botox Consultation'
        },
        volume: {
            title: 'Dermal Fillers & Sculptra',
            description: 'Restore lost volume and stimulate natural collagen production.',
            treatments: [
                { name: 'Lip Enhancement', desc: 'Natural-looking volume', icon: 'fa-lips' },
                { name: 'Cheek Contour', desc: 'Restore youthful fullness', icon: 'fa-face-kiss-wink-heart' },
                { name: 'Sculptra', desc: 'Long-lasting collagen stimulation', icon: 'fa-seedling' }
            ],
            cta: 'Book Filler Consultation'
        },
        skin: {
            title: 'Laser & Skin Rejuvenation',
            description: 'Even skin tone, reduce sun damage, and reveal radiant skin.',
            treatments: [
                { name: 'ClearLift Laser', desc: 'No-downtime skin resurfacing', icon: 'fa-sun' },
                { name: 'CO2 CoolPeel', desc: 'Advanced skin rejuvenation', icon: 'fa-fire' },
                { name: 'Microneedling', desc: 'Collagen induction therapy', icon: 'fa-spa' }
            ],
            cta: 'Book Skin Consultation'
        },
        weight: {
            title: 'Medical Weight Loss & Body Contouring',
            description: 'Achieve your body goals with medical-grade treatments.',
            treatments: [
                { name: 'Medical Weight Loss', desc: 'Semaglutide/Tirzepatide programs', icon: 'fa-weight-scale' },
                { name: 'Body Contouring', desc: 'Non-invasive fat reduction', icon: 'fa-person' },
                { name: 'Lipo Shots', desc: 'Boost metabolism & energy', icon: 'fa-syringe' }
            ],
            cta: 'Book Weight Loss Consultation'
        },
        energy: {
            title: 'IV Therapy & Wellness',
            description: 'Replenish from within and boost your vitality.',
            treatments: [
                { name: 'NAD+ Therapy', desc: 'Cellular rejuvenation', icon: 'fa-bolt' },
                { name: 'Myers Cocktail', desc: 'Ultimate wellness boost', icon: 'fa-heart' },
                { name: 'Vitamin B12', desc: 'Energy & metabolism support', icon: 'fa-sun' }
            ],
            cta: 'Book IV Therapy'
        },
        hair: {
            title: 'Laser Hair Removal',
            description: 'Permanent hair reduction for smooth, hair-free skin.',
            treatments: [
                { name: 'Small Area', desc: 'Upper lip, chin, or underarms', icon: 'fa-wand-magic-sparkles' },
                { name: 'Medium Area', desc: 'Bikini line or half legs', icon: 'fa-leaf' },
                { name: 'Large Area', desc: 'Full legs or back', icon: 'fa-gem' }
            ],
            cta: 'Book Laser Consultation'
        }
    };

    function updateProgress() {
        const progress = (currentStep / totalSteps) * 100;
        progressFill.style.width = `${progress}%`;
        currentStepEl.textContent = currentStep;
    }

    function showStep(step) {
        steps.forEach(s => s.classList.remove('active'));
        const targetStep = document.querySelector(`.quiz-step[data-step="${step}"]`);
        if (targetStep) {
            targetStep.classList.add('active');
        }
        
        // Update buttons
        prevBtn.style.display = step > 1 ? 'inline-flex' : 'none';
        
        if (step === totalSteps) {
            nextBtn.innerHTML = 'Get My Recommendations <i class="fas fa-sparkles"></i>';
        } else {
            nextBtn.innerHTML = 'Continue <i class="fas fa-arrow-right"></i>';
        }
        
        updateProgress();
    }

    function validateCurrentStep() {
        const currentStepEl = document.querySelector(`.quiz-step[data-step="${currentStep}"]`);
        const inputs = currentStepEl.querySelectorAll('input[required], textarea[required]');
        
        for (let input of inputs) {
            if (input.type === 'radio') {
                const name = input.name;
                const checked = currentStepEl.querySelector(`input[name="${name}"]:checked`);
                if (!checked) return false;
            } else if (!input.value.trim()) {
                input.focus();
                return false;
            }
        }
        return true;
    }

    function collectFormData() {
        const formElements = quizForm.elements;
        for (let element of formElements) {
            if (element.name && element.value) {
                if (element.type === 'radio' && element.checked) {
                    formData[element.name] = element.value;
                } else if (element.type === 'checkbox') {
                    formData[element.name] = element.checked;
                } else if (element.type !== 'radio') {
                    formData[element.name] = element.value;
                }
            }
        }
    }

    function generateRecommendations() {
        const concern = formData.concern;
        const rec = recommendations[concern] || recommendations.wrinkles;
        
        const recommendationsHTML = `
            <div class="primary-recommendation">
                <h3><i class="fas fa-star"></i> Recommended For You</h3>
                <div class="recommendation-card featured">
                    <h4>${rec.title}</h4>
                    <p>${rec.description}</p>
                    <div class="recommended-treatments">
                        ${rec.treatments.map(t => `
                            <div class="treatment-item">
                                <i class="fas ${t.icon}"></i>
                                <div>
                                    <strong>${t.name}</strong>
                                    <span>${t.desc}</span>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
            <div class="next-steps">
                <h4>Your Next Steps</h4>
                <div class="steps-list">
                    <div class="step-item">
                        <div class="step-icon">1</div>
                        <p>Book a complimentary consultation to discuss your personalized treatment plan</p>
                    </div>
                    <div class="step-item">
                        <div class="step-icon">2</div>
                        <p>Meet with our expert providers for a thorough assessment</p>
                    </div>
                    <div class="step-item">
                        <div class="step-icon">3</div>
                        <p>Begin your transformation journey with treatments tailored to your goals</p>
                    </div>
                </div>
            </div>
        `;
        
        document.getElementById('recommendationsList').innerHTML = recommendationsHTML;
    }

    function showResults() {
        steps.forEach(s => s.classList.remove('active'));
        document.querySelector('.quiz-step[data-step="results"]').classList.add('active');
        quizNav.style.display = 'none';
        document.querySelector('.quiz-progress').style.display = 'none';
        generateRecommendations();
        
        // Scroll to results
        document.querySelector('.quiz-step[data-step="results"]').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    nextBtn.addEventListener('click', function() {
        if (!validateCurrentStep()) {
            // Shake animation for invalid
            const currentStepEl = document.querySelector(`.quiz-step[data-step="${currentStep}"]`);
            currentStepEl.style.animation = 'shake 0.5s';
            setTimeout(() => {
                currentStepEl.style.animation = '';
            }, 500);
            return;
        }
        
        collectFormData();
        
        if (currentStep < totalSteps) {
            currentStep++;
            showStep(currentStep);
        } else {
            showResults();
        }
    });

    prevBtn.addEventListener('click', function() {
        if (currentStep > 1) {
            currentStep--;
            showStep(currentStep);
        }
    });

    // Allow clicking on options to proceed (optional enhancement)
    document.querySelectorAll('.quiz-option input[type="radio"]').forEach(radio => {
        radio.addEventListener('change', function() {
            // Optional: auto-advance after selection
            // setTimeout(() => nextBtn.click(), 300);
        });
    });

    // Phone number formatting
    const phoneInput = document.getElementById('phone');
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length >= 6) {
                value = `(${value.slice(0, 3)}) ${value.slice(3, 6)}-${value.slice(6, 10)}`;
            } else if (value.length >= 3) {
                value = `(${value.slice(0, 3)}) ${value.slice(3)}`;
            }
            e.target.value = value;
        });
    }

    // Initialize
    updateProgress();
})();
