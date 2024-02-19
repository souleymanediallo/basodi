document.addEventListener('DOMContentLoaded', function() {
    // Fonction pour convertir les noms de catégorie et de sous-catégorie en type_choice
    function convertSubCategoryToTypeChoice(subCategoryName, mainCategoryName) {
        var typeChoice = '';
        if (mainCategoryName === 'Femmes' && subCategoryName === 'Vêtements') {
        typeChoice = 'Vêtements-Femmes';
            }
        else if (mainCategoryName === 'Hommes' && subCategoryName === 'Vêtements') {
                typeChoice = 'Vêtements-Hommes';
            }
        else if (mainCategoryName === 'Femmes' && subCategoryName === 'Chaussures') {
                typeChoice = 'Chaussures-Femmes';
            }
        else if (mainCategoryName === 'Hommes' && subCategoryName === 'Chaussures') {
                typeChoice = 'Chaussures-Hommes';
            }
        return typeChoice;
    }

    // Gestionnaire de changement pour la catégorie principale
    var mainCategorySelect = document.getElementById('main_category_select');
    if (mainCategorySelect) {
        mainCategorySelect.addEventListener('change', function() {
            // Votre logique existante pour charger les sous-catégories
        });
    }

    // Gestionnaire de changement pour la sous-catégorie
    var subCategorySelect = document.getElementById('sub_category_select');
    if (subCategorySelect) {
        subCategorySelect.addEventListener('change', function() {
            // Votre logique existante pour charger les troisièmes sous-catégories

            // Déplacez la logique suivante dans le gestionnaire d'événements pour la sous-catégorie
            var mainCategoryName = mainCategorySelect.options[mainCategorySelect.selectedIndex].text;
            var subCategoryName = subCategorySelect.options[subCategorySelect.selectedIndex].text;
            var typeChoice = convertSubCategoryToTypeChoice(subCategoryName, mainCategoryName);

            fetch(`api/get-sizes/${typeChoice}/`)
                .then(response => response.json())
                .then(sizes => {
                    var sizeSelect = document.getElementById('size_select');
                    sizeSelect.innerHTML = ''; // Vider les options existantes
                    sizes.forEach(function(size) {
                        var option = new Option(size.name, size.id);
                        sizeSelect.appendChild(option);
                    });
                    sizeSelect.parentElement.style.display = sizes.length > 0 ? 'block' : 'none';
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    }
});
