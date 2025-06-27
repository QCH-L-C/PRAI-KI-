// Seiten-spezifisches Skript für PRAI-OS
document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('code-toggle-button');
    const codeSection = document.getElementById('code-details-section');

    if (toggleButton && codeSection) {
        toggleButton.addEventListener('click', () => {
            const isHidden = codeSection.classList.contains('is-hidden');
            if (isHidden) {
                codeSection.classList.remove('is-hidden');
                toggleButton.textContent = 'Hide Details';
            } else {
                codeSection.classList.add('is-hidden');
                toggleButton.textContent = 'Show Details';
            }
        });
    }
});
