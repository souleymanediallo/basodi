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
});