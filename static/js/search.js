$(function() {
  var price_range = [ 300, 90000 ];
  var bedroom_range = [2, 7]

  // For price in search form
  $( "#price-slider-range" ).slider({
    range: true,
    min: 100,
    max: 99999,
    values: price_range,
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
    values: bedroom_range,
    slide: function( event, ui ) {
      $( "#property_bedroom_low" ).val( ui.values[ 0 ] );
      $( "#property_bedroom_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#property_bedroom_low" ).val( $( "#bedroom-slider-range" ).slider( "values", 0 ) );
  $( "#property_bedroom_high" ).val( $( "#bedroom-slider-range" ).slider( "values", 1 ) );

  // For price in search form for rent
  $( "#rent-price-slider-range" ).slider({
    range: true,
    min: 100,
    max: 99999,
    values: price_range,
    slide: function( event, ui ) {
      val_str = ui.values[ 0 ]+'';
      $( "#rent-property_price_low" ).val( val_str );
      $( "#rent-property_price_low" ).width(8*val_str.length);
      $( "#rent-property_price_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#rent-property_price_low" ).val( $( "#rent-price-slider-range" ).slider( "values", 0 ) );
  $( "#rent-property_price_high" ).val( $( "#rent-price-slider-range" ).slider( "values", 1 ) );

  // for bedroom in search form for rent
  $( "#rent-bedroom-slider-range" ).slider({
    range: true,
    min: 1,
    max: 12,
    values: bedroom_range,
    slide: function( event, ui ) {
      $( "#rent-property_bedroom_low" ).val( ui.values[ 0 ] );
      $( "#rent-property_bedroom_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#rent-property_bedroom_low" ).val( $( "#rent-bedroom-slider-range" ).slider( "values", 0 ) );
  $( "#rent-property_bedroom_high" ).val( $( "#rent-bedroom-slider-range" ).slider( "values", 1 ) );
});

function search_residental(form_id)
{
  $.post('/residential/properties/', $('#'+form_id).serialize())
  .success(function(result){
    $('.middle').html(result);
  });
}