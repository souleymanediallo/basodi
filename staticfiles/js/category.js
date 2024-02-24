document.addEventListener('DOMContentLoaded', function() {
    // Lorsque la catégorie principale change
    document.getElementById('main_category_select').addEventListener('change', function() {
        var genderName = this.options[this.selectedIndex].text;
        fetch(`api/get-categories-for-gender/${genderName}/`)
            .then(response => response.json())
            .then(data => {
                var subCategorySelect = document.getElementById('sub_category_select');
                subCategorySelect.innerHTML = '';
                data.forEach(function(category) {
                    var option = new Option(category.name, category.id);
                    subCategorySelect.add(option);
                });
            });
    });

    // Lorsque la sous-catégorie change
    document.getElementById('sub_category_select').addEventListener('change', function() {
        var categoryId = this.value;
        fetch(`api/get-subcategories-for-category/${categoryId}/`)
            .then(response => response.json())
            .then(data => {
                var thirdSubCategorySelect = document.getElementById('third_sub_category_select');
                thirdSubCategorySelect.innerHTML = '';
                data.forEach(function(subcategory) {
                    var option = new Option(subcategory.name, subcategory.id);
                    thirdSubCategorySelect.add(option);
                });
            });
    });

    // size select
    document.getElementById('sub_category_select').addEventListener('change', function() {
    var subCategoryName = this.options[this.selectedIndex].text;
    // Convertir le nom de la sous-catégorie en un type de taille attendu par l'API
    var typeChoice = convertSubCategoryToTypeChoice(subCategoryName);

    fetch(`/api/get-sizes/${typeChoice}/`)
        .then(response => response.json())
        .then(sizes => {
            var sizeSelect = document.getElementById('size_select');
            sizeSelect.innerHTML = ''; // Vider les options existantes
            sizes.forEach(function(size) {
                var option = new Option(size.name, size.id);
                sizeSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

function convertSubCategoryToTypeChoice(subCategoryName) {
    // Votre logique ici pour convertir le nom de la sous-catégorie en type de taille
    // Par exemple, si subCategoryName est "Chaussures-Femmes", renvoyez cette chaîne.
    return subCategoryName;
}



});