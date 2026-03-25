// AI Prompt Optimizer - Main JavaScript

// Copy to clipboard function
function copyToClipboard(text) {
    const tempInput = document.createElement('textarea');
    tempInput.value = text;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
}

// Show toast notification
function showToast(message, type = 'success') {
    alert(message); // Simple alert for now
}

// Format date nicely
function formatDate(dateString) {
    const date = new Date(dateString);
    const options = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    return date.toLocaleDateString('en-US', options);
}

// Truncate text
function truncateText(text, maxLength = 100) {
    if (text.length <= maxLength) return text;
    return text.substring(0, maxLength) + '...';
}

// Smooth scroll to element
function scrollToElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

// Auto-dismiss only error alerts (keep results visible)
document.addEventListener('DOMContentLoaded', function() {
    const errorAlerts = document.querySelectorAll('.alert-danger, .alert-warning');
    errorAlerts.forEach(function(alert) {
        // Removed auto-dismiss timeout - errors stay visible
    });
});

// Prevent double form submission
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                // Removed timeout - button disabled until server responds
            }
        });
    });
});

// Character counter for textareas
function addCharacterCounter(textareaId, maxChars = 2000) {
    const textarea = document.getElementById(textareaId);
    if (!textarea) return;

    const counter = document.createElement('div');
    counter.className = 'form-text text-end';
    counter.id = textareaId + '_counter';
    textarea.parentNode.insertBefore(counter, textarea.nextSibling);

    function updateCounter() {
        const remaining = maxChars - textarea.value.length;
        counter.textContent = `${textarea.value.length} / ${maxChars} characters`;
        if (remaining < 100) {
            counter.classList.add('text-danger');
        } else {
            counter.classList.remove('text-danger');
        }
    }

    textarea.addEventListener('input', updateCounter);
    updateCounter();
}

// Add character counter to userInput on dashboard
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('userInput')) {
        addCharacterCounter('userInput', 2000);
    }
});

// Console welcome message
console.log('%cAI Prompt Optimizer', 'color: #198754; font-size: 20px; font-weight: bold;');
console.log('%cBuilt by Prakash', 'color: #6c757d; font-size: 12px;');
console.log('%cDjango + Bootstrap + Free AI APIs', 'color: #0d6efd; font-size: 12px;');