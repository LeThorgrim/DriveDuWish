document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.sidebar a');
    const contentSections = document.querySelectorAll('.content-section');

    // Masquer toutes les sections de contenu
    contentSections.forEach(section => section.style.display = 'none');

    // Afficher la section de contenu "accueil"
    const accueilSection = document.getElementById('content-home');
    if (accueilSection) {
        accueilSection.style.display = 'block';
    }

    menuItems.forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault();

            // Masquer toutes les sections de contenu
            contentSections.forEach(section => section.style.display = 'none');

            // Afficher la section de contenu correspondante
            const contentId = 'content-' + item.id;
            document.getElementById(contentId).style.display = 'block';
        });
    });
});