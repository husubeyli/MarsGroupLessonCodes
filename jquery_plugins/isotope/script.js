var $grid = $('.grid').isotope({
  });

$('.filter-button-group').on( 'click', 'button', function() {
    var filterValue = $(this).attr('data-filter');
    $grid.isotope({ filter: filterValue });
});



// $grid.isotope({ filter: '.front-end' });