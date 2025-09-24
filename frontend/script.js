// ===== ELIS FRONTEND - INTERACTIVE JAVASCRIPT =====
class ElisApp {
    constructor() {
        // Configuration
        this.config = {
            apiBaseUrl: 'http://127.0.0.1:8000', // Update this for production
            apiKey: 'your-api-key-here', // Will be replaced with actual key
            endpoints: {
                therapists: '/therapists'
            }
        };
        
        // DOM Elements
        this.elements = {
            searchForm: document.getElementById('searchForm'),
            searchButton: document.getElementById('searchButton'),
            buttonText: document.querySelector('.button-text'),
            buttonLoader: document.getElementById('buttonLoader'),
            resultsSection: document.getElementById('resultsSection'),
            resultsContainer: document.getElementById('resultsContainer'),
            districtSelect: document.getElementById('district'),
            methodSelect: document.getElementById('method'),
            experienceSelect: document.getElementById('experience')
        };
        
        // State
        this.isLoading = false;
        this.lastSearchParams = null;
        
        // Initialize the app
        this.init();
    }
    
    init() {
        console.log('🚀 ELIS App initialized');
        this.bindEvents();
        this.setupFormValidation();
    }
    
    bindEvents() {
        // Search form submission
        this.elements.searchForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleSearch();
        });
        
        // Auto-search on select change (optional UX enhancement)
        [this.elements.districtSelect, this.elements.methodSelect, this.elements.experienceSelect]
            .forEach(select => {
                select.addEventListener('change', () => {
                    // Auto-search if at least one field is selected
                    if (this.hasSearchCriteria()) {
                        this.handleSearch();
                    }
                });
            });
    }
    
    setupFormValidation() {
        // Add visual feedback for form interactions
        const selects = this.elements.searchForm.querySelectorAll('select');
        selects.forEach(select => {
            select.addEventListener('focus', () => {
                select.parentElement.classList.add('focused');
            });
            
            select.addEventListener('blur', () => {
                select.parentElement.classList.remove('focused');
            });
        });
    }
    
    hasSearchCriteria() {
        return this.elements.districtSelect.value || 
               this.elements.methodSelect.value || 
               this.elements.experienceSelect.value;
    }
    
    async handleSearch() {
        if (this.isLoading) return;
        
        try {
            // Show loading state
            this.setLoadingState(true);
            
            // Get search parameters
            const searchParams = this.getSearchParameters();
            this.lastSearchParams = searchParams;
            
            console.log('🔍 Searching with params:', searchParams);
            
            // Make API request
            const therapists = await this.searchTherapists(searchParams);
            
            console.log(`✅ Found ${therapists.length} therapists`);
            
            // Display results
            this.displayResults(therapists);
            
            // Smooth scroll to results
            this.scrollToResults();
            
        } catch (error) {
            console.error('❌ Search failed:', error);
            this.displayError(error);
        } finally {
            this.setLoadingState(false);
        }
    }
    
    getSearchParameters() {
        const params = new URLSearchParams();
        
        const district = this.elements.districtSelect.value;
        const method = this.elements.methodSelect.value;
        const experience = this.elements.experienceSelect.value;
        
        if (district) params.append('district', district);
        if (method) params.append('method', method);
        if (experience) params.append('min_experience', experience);
        
        return params;
    }
    
    async searchTherapists(searchParams) {
        const url = `${this.config.apiBaseUrl}${this.config.endpoints.therapists}?${searchParams}`;
        
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'X-API-Key': this.config.apiKey // Include API key when implemented
            }
        });
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || `HTTP ${response.status}: ${response.statusText}`);
        }
        
        return await response.json();
    }
    
    displayResults(therapists) {
        this.elements.resultsContainer.innerHTML = '';
        
        if (therapists.length === 0) {
            this.displayEmptyState();
            return;
        }
        
        // Create therapist cards
        therapists.forEach((therapist, index) => {
            const card = this.createTherapistCard(therapist, index);
            this.elements.resultsContainer.appendChild(card);
        });
        
        // Show results section
        this.elements.resultsSection.style.display = 'block';
    }
    
    createTherapistCard(therapist, index) {
        const card = document.createElement('div');
        card.className = 'therapist-card';
        card.style.setProperty('--delay', index);
        
        // Generate initials for avatar
        const initials = this.generateInitials(therapist.first_name, therapist.last_name);
        
        // Calculate years of experience
        const experience = this.calculateExperience(therapist.registration_date);
        
        card.innerHTML = `
            <div class="therapist-header">
                <div class="therapist-avatar">${initials}</div>
                <div>
                    <h3 class="therapist-name">${this.escapeHtml(therapist.first_name)} ${this.escapeHtml(therapist.last_name)}</h3>
                    <p class="therapist-title">${this.escapeHtml(therapist.title || 'Therapist')}</p>
                </div>
            </div>
            <div class="therapist-details">
                <div class="detail-item">
                    <span class="detail-icon">🏥</span>
                    <span>Method: ${this.escapeHtml(therapist.therapy_methods)}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-icon">📍</span>
                    <span>District: ${this.escapeHtml(therapist.postal_code)} ${this.escapeHtml(therapist.state)}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-icon">⏱️</span>
                    <span>Experience: ${experience} years</span>
                </div>
                <div class="detail-item">
                    <span class="detail-icon">📧</span>
                    <span>${this.escapeHtml(therapist.email)}</span>
                </div>
            </div>
        `;
        
        return card;
    }
    
    displayEmptyState() {
        this.elements.resultsContainer.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">🔍</div>
                <h3 class="empty-state-title">No therapists found</h3>
                <p class="empty-state-message">
                    Try adjusting your search criteria or browse all available therapists.
                </p>
            </div>
        `;
        this.elements.resultsSection.style.display = 'block';
    }
    
    displayError(error) {
        this.elements.resultsContainer.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">⚠️</div>
                <h3 class="empty-state-title">Search Error</h3>
                <p class="empty-state-message">
                    ${this.escapeHtml(error.message)}<br>
                    Please try again or contact support if the problem persists.
                </p>
            </div>
        `;
        this.elements.resultsSection.style.display = 'block';
    }
    
    setLoadingState(loading) {
        this.isLoading = loading;
        
        if (loading) {
            this.elements.searchButton.classList.add('loading');
            this.elements.searchButton.disabled = true;
        } else {
            this.elements.searchButton.classList.remove('loading');
            this.elements.searchButton.disabled = false;
        }
    }
    
    scrollToResults() {
        setTimeout(() => {
            this.elements.resultsSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }, 100);
    }
    
    // Utility Functions
    generateInitials(firstName, lastName) {
        const first = firstName?.charAt(0)?.toUpperCase() || '';
        const last = lastName?.charAt(0)?.toUpperCase() || '';
        return first + last || '?';
    }
    
    calculateExperience(registrationDate) {
        if (!registrationDate) return 'Unknown';
        
        const regDate = new Date(registrationDate);
        const currentDate = new Date();
        const diffTime = Math.abs(currentDate - regDate);
        const diffYears = Math.floor(diffTime / (1000 * 60 * 60 * 24 * 365));
        
        return diffYears;
    }
    
    escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    // Public methods for external use
    clearResults() {
        this.elements.resultsContainer.innerHTML = '';
        this.elements.resultsSection.style.display = 'none';
    }
    
    resetForm() {
        this.elements.searchForm.reset();
        this.clearResults();
    }
}

// ===== ENHANCED UX FEATURES =====
class UXEnhancements {
    static init() {
        this.addSmoothScrolling();
        this.addFormAnimations();
        this.addKeyboardShortcuts();
    }
    
    static addSmoothScrolling() {
        // Smooth scrolling for any anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });
    }
    
    static addFormAnimations() {
        // Add focus animations to form elements
        const formGroups = document.querySelectorAll('.form-group');
        formGroups.forEach(group => {
            const select = group.querySelector('select');
            if (select) {
                select.addEventListener('focus', () => {
                    group.style.transform = 'translateY(-2px)';
                });
                
                select.addEventListener('blur', () => {
                    group.style.transform = 'translateY(0)';
                });
            }
        });
    }
    
    static addKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Ctrl/Cmd + Enter to submit search
            if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
                e.preventDefault();
                document.getElementById('searchButton').click();
            }
            
            // Escape to clear search
            if (e.key === 'Escape') {
                window.elisApp?.resetForm();
            }
        });
    }
}

// ===== APP INITIALIZATION =====
document.addEventListener('DOMContentLoaded', () => {
    console.log('🌟 ELIS Frontend Loading...');
    
    // Initialize the main app
    window.elisApp = new ElisApp();
    
    // Initialize UX enhancements
    UXEnhancements.init();
    
    console.log('✨ ELIS Frontend Ready!');
});

// ===== DEVELOPMENT HELPERS =====
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    // Development mode logging
    window.addEventListener('load', () => {
        console.log('%c🎉 ELIS Development Mode', 'color: #6366f1; font-weight: bold; font-size: 16px;');
        console.log('%cAPI Base URL:', 'font-weight: bold;', window.elisApp?.config.apiBaseUrl);
        console.log('%cTip: Open DevTools Network tab to monitor API requests', 'color: #666; font-style: italic;');
    });
}