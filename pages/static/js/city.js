var data = [];
$.getJSON('file:///Users/souleymane/PycharmProjects/basodi/accounts/data-city.json', function (result) {
    .$each(result.cities, function (index, val) {
        data.push(val);
    }
}

  $( "#auto_check" ).autocomplete({
      source: data
    });

// Path: pages/static/js/city.js
