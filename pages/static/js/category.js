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
    var subCategory = this.value;
    console.log("SubCategory selected:", subCategory); // Débogage

    fetch(`/api/get-sizes/${subCategory}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
            return response.json();
        })
        .then(sizes => {
            console.log("Sizes received:", sizes); // Débogage
            var sizeSelect = document.getElementById('size_select');
            sizeSelect.innerHTML = ''; // Vider les options existantes
            sizes.forEach(function(size) {
                var option = new Option(size.name, size.id);
                sizeSelect.add(option);
            });
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
});


});