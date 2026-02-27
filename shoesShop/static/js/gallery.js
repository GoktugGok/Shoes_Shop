function applyFilterShoes(config) {
    // Get the current primary category from context OR selected checkbox
    var selectedCategories = [];
    $("input[name='shoesCategory']:checked").each(function () {
        selectedCategories.push($(this).val());
    });

    // Use the first selected category as primary, or the default one from config
    var category = selectedCategories.length > 0 ? selectedCategories[0] : config.defaultCategory;

    // Update UI breadcrumb
    if (selectedCategories.length > 0) {
        $('#activeCategory').text($("input[name='shoesCategory']:checked").next('label').text());
    } else {
        $('#activeCategory').text(config.defaultCategoryTitle);
    }

    var Shoe_Height_filterValues = [];
    $("input[name='ShoeHeight']:checked").each(function () {
        Shoe_Height_filterValues.push($(this).val());
    });

    var shoes_color_filterValues = [];
    $("input[name='shoesColor']:checked").each(function () {
        shoes_color_filterValues.push($(this).val());
    });

    var shoes_number_filterValues = [];
    $("input[name='shoesNumber']:checked").each(function () {
        shoes_number_filterValues.push($(this).val());
    });

    var shoes_brand_filterValues = [];
    $("input[name='brand']:checked").each(function () {
        shoes_brand_filterValues.push($(this).val());
    });

    var url = config.filterUrl + "?category_name=" + category;
    Shoe_Height_filterValues.forEach(val => url += "&shoe_height_filters=" + val);
    shoes_color_filterValues.forEach(val => url += "&shoes_color_filters=" + val);
    shoes_number_filterValues.forEach(val => url += "&shoes_number_filters=" + val);
    shoes_brand_filterValues.forEach(val => url += "&shoes_brand_filters=" + val);

    var shoesHtml = '';
    $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            $('#shoes-container').empty();
            $('#countS').html(response.shoes_count);
            response.shoes.forEach(function (shoe) {
                var shoeUrl = config.productUrlBase.replace('0', shoe.id);
                shoesHtml += `
                  <div class="col-sm-6 col-lg-4 col-xl-3">
                     <a href="${shoeUrl}" class="text-decoration-none">
                        <div class="product-card-v2">
                           <div class="badge-new">PREMIUM</div>
                           <div class="p-img-wrapper">
                              <img src="/media/${shoe.image}" alt="${shoe.name}">
                           </div>
                           <div class="p-content">
                              <div>
                                 <div class="p-category">Footwear</div>
                                 <h3 class="p-name">${shoe.name}</h3>
                              </div>
                              <div class="p-footer">
                                 <div class="p-price">₺${shoe.price}</div>
                                 <div class="p-btn-view">
                                    <i class="bi bi-arrow-right"></i>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </a>
                  </div>`;
            });
            $('#shoes-container').html(shoesHtml);
        }
    });
}

// Initialize Gallery Collapse/Chevron Logic
function initGalleryFilters() {
    document.querySelectorAll('.filter-title').forEach(function (btn) {
        var targetSelector = btn.getAttribute('data-bs-target');
        if (!targetSelector) return;
        var target = document.querySelector(targetSelector);
        var icon = btn.querySelector('i');
        if (!target || !icon) return;

        // initialize icon based on current state
        if (target.classList.contains('show')) {
            icon.classList.remove('bi-chevron-down'); icon.classList.add('bi-chevron-up');
        } else {
            icon.classList.remove('bi-chevron-up'); icon.classList.add('bi-chevron-down');
        }

        // create/get Bootstrap Collapse instance
        var collapseInstance = bootstrap.Collapse.getOrCreateInstance(target, { toggle: false });

        // toggle via API when title clicked
        btn.addEventListener('click', function (e) {
            collapseInstance.toggle();
        });

        // update icon when collapse finishes
        target.addEventListener('shown.bs.collapse', function () {
            icon.classList.remove('bi-chevron-down'); icon.classList.add('bi-chevron-up');
        });
        target.addEventListener('hidden.bs.collapse', function () {
            icon.classList.remove('bi-chevron-up'); icon.classList.add('bi-chevron-down');
        });
    });
}
