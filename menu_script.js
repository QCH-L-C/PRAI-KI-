// MANIFEST: Nur Menü-Logik, da keine Suche auf dieser Seite vorhanden ist.
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('hamburger');
    const navList = document.getElementById('navLinks');

    // Toggle für das mobile Menü
    if (hamburger && navList) {
        hamburger.addEventListener('click', (e) => {
            // Verhindert, dass der Klick sofort das Menü wieder schließt, falls er sich zum Body propagiert
            e.stopPropagation(); 
            navList.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
    }

    // Schließe das Menü bei Klick auf einen Link oder außerhalb
    document.addEventListener('click', (event) => {
        if (navList.classList.contains('active')) {
            // Prüft, ob der Klick außerhalb der Navigation und des Hamburgers war
            if (!navList.contains(event.target) && !hamburger.contains(event.target)) {
                navList.classList.remove('active');
                hamburger.classList.remove('active');
            }
        }
    });
});
