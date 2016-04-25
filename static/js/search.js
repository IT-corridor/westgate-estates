$(function() {
  // For price in search form
  $( "#price-slider-range" ).slider({
    range: true,
    min: 100,
    max: 99999,
    values: [ 300, 90000 ],
    slide: function( event, ui ) {
      val_str = ui.values[ 0 ]+'';
      $( "#property_price_low" ).val( val_str );
      $( "#property_price_low" ).width(8*val_str.length);
      $( "#property_price_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#property_price_low" ).val( $( "#price-slider-range" ).slider( "values", 0 ) );
  $( "#property_price_high" ).val( $( "#price-slider-range" ).slider( "values", 1 ) );

  // for bedroom in search form
  $( "#bedroom-slider-range" ).slider({
    range: true,
    min: 1,
    max: 12,
    values: [ 2, 7 ],
    slide: function( event, ui ) {
      $( "#property_bedroom_low" ).val( ui.values[ 0 ] );
      $( "#property_bedroom_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#property_bedroom_low" ).val( $( "#bedroom-slider-range" ).slider( "values", 0 ) );
  $( "#property_bedroom_high" ).val( $( "#bedroom-slider-range" ).slider( "values", 1 ) );

});