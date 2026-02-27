$(document).ready(function () {
   // Smooth scroll for anchors
   $('a[href^="#"]').on('click', function (event) {
      var target = $(this.getAttribute('href'));
      if (target.length) {
         event.preventDefault();
         $('html, body').stop().animate({
            scrollTop: target.offset().top - 100
         }, 800);
      }
   });

   $(".fancybox").fancybox({
      openEffect: "none",
      closeEffect: "none"
   });

   $('#myCarousel').carousel({
      interval: false
   });
});

function openNav() {
   document.getElementById("mySidebar").style.width = "250px";
   document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
   document.getElementById("mySidebar").style.width = "0";
   document.getElementById("main").style.marginLeft = "0";
}

function applySearchResults(config) {
   var searchTerm = document.getElementById("searchInput").value;
   var searchResults = document.getElementById("searchResults");
   if (!searchTerm) {
      searchResults.classList.add("visually-hidden-focusable");
      return;
   }
   $.ajax({
      type: "GET",
      url: config.searchUrl,
      data: { 'q': searchTerm },
      success: function (response) {
         if (response.success && response.data.shoes_filter.length > 0) {
            searchResults.classList.remove("visually-hidden-focusable");
            searchResults.innerHTML = "";
            response.data.shoes_filter.forEach(shoe => {
               let product_url = config.productUrlBase.replace('0', shoe.id);
               searchResults.innerHTML += `
                  <li>
                     <a href="${product_url}" class="search_item">
                        <img src="/media/${shoe.image}" alt="${shoe.name}" class="search-thumb">
                        <div class="flex-grow-1">
                           <div class="search-title">${shoe.name}</div>
                           ${shoe.price ? `<div class="search-price">₺${shoe.price}</div>` : ''}
                        </div>
                     </a>
                  </li>`;
            });
         } else {
            searchResults.classList.add("visually-hidden-focusable");
         }
      }
   });
}

// Close search results when clicking outside
$(document).on('click', function (e) {
   if (!$(e.target).closest('.search-wrapper').length) {
      $('#searchResults').addClass('visually-hidden-focusable');
   }
});
// Global Slider Scroll Function
function scrollSlider(direction, id) {
   const slider = document.getElementById(id);
   if (!slider) return;
   const scrollAmount = slider.clientWidth * 0.8;
   if (direction === 'left') {
      slider.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
   } else {
      slider.scrollBy({ left: scrollAmount, behavior: 'smooth' });
   }
}
