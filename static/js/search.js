$(function() {
  // For sale price in search form
  $( "#price-slider-range" ).slider({
    range: true,
    min: sprice_min,
    max: sprice_max,
    values: price_range_sale,
    slide: function( event, ui ) {
      val_str = ui.values[ 0 ]+'';
      $( "#property_price_low" ).val( val_str );
      $( "#property_price_low" ).width(8*val_str.length);
      $( "#property_price_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#property_price_low" ).val( $( "#price-slider-range" ).slider( "values", 0 ) );
  $( "#property_price_high" ).val( $( "#price-slider-range" ).slider( "values", 1 ) );

  // for sale bedroom in search form
  $( "#bedroom-slider-range" ).slider({
    range: true,
    min: sbedroom_min,
    max: sbedroom_max,
    values: bedroom_range_sale,
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
    min: rprice_min,
    max: rprice_max,
    values: price_range_rent,
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
    min: rbedroom_min,
    max: rbedroom_max,
    values: bedroom_range_rent,
    slide: function( event, ui ) {
      $( "#rent-property_bedroom_low" ).val( ui.values[ 0 ] );
      $( "#rent-property_bedroom_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#rent-property_bedroom_low" ).val( $( "#rent-bedroom-slider-range" ).slider( "values", 0 ) );
  $( "#rent-property_bedroom_high" ).val( $( "#rent-bedroom-slider-range" ).slider( "values", 1 ) );

  $('#let_furn_rent').val(let_furn);

  // Commercial
  // For sale price in search form
  $( "#cprice-slider-range" ).slider({
    range: true,
    min: csprice_min,
    max: csprice_max,
    values: cprice_range_sale,
    slide: function( event, ui ) {
      val_str = ui.values[ 0 ]+'';
      $( "#cproperty_price_low" ).val( val_str );
      $( "#cproperty_price_low" ).width(8*val_str.length);
      $( "#cproperty_price_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#cproperty_price_low" ).val( $( "#cprice-slider-range" ).slider( "values", 0 ) );
  $( "#cproperty_price_high" ).val( $( "#cprice-slider-range" ).slider( "values", 1 ) );

  // for sale bedroom in search form
  $( "#cbedroom-slider-range" ).slider({
    range: true,
    min: csbedroom_min,
    max: csbedroom_max,
    values: cbedroom_range_sale,
    slide: function( event, ui ) {
      $( "#cproperty_bedroom_low" ).val( ui.values[ 0 ] );
      $( "#cproperty_bedroom_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#cproperty_bedroom_low" ).val( $( "#cbedroom-slider-range" ).slider( "values", 0 ) );
  $( "#cproperty_bedroom_high" ).val( $( "#cbedroom-slider-range" ).slider( "values", 1 ) );

  // For price in search form for rent
  $( "#crent-price-slider-range" ).slider({
    range: true,
    min: crprice_min,
    max: crprice_max,
    values: cprice_range_rent,
    slide: function( event, ui ) {
      val_str = ui.values[ 0 ]+'';
      $( "#crent-property_price_low" ).val( val_str );
      $( "#crent-property_price_low" ).width(8*val_str.length);
      $( "#crent-property_price_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#crent-property_price_low" ).val( $( "#crent-price-slider-range" ).slider( "values", 0 ) );
  $( "#crent-property_price_high" ).val( $( "#crent-price-slider-range" ).slider( "values", 1 ) );

  // for bedroom in search form for rent
  $( "#crent-bedroom-slider-range" ).slider({
    range: true,
    min: crbedroom_min,
    max: crbedroom_max,
    values: cbedroom_range_rent,
    slide: function( event, ui ) {
      $( "#crent-property_bedroom_low" ).val( ui.values[ 0 ] );
      $( "#crent-property_bedroom_high" ).val( ui.values[ 1 ] );
    }
  });
  $( "#crent-property_bedroom_low" ).val( $( "#crent-bedroom-slider-range" ).slider( "values", 0 ) );
  $( "#crent-property_bedroom_high" ).val( $( "#crent-bedroom-slider-range" ).slider( "values", 1 ) );

  $('#clet_furn_rent').val(clet_furn);

});

// not used
function search_residental(form_id)
{
  $.post('/residential/properties/', $('#'+form_id).serialize())
  .success(function(result){
    $('.middle').html(result);
  });
}

function login_check(e, logged_in)
{
  if (logged_in === 'False')
  {
    e.stopPropagation();    
    $( "#dialog-confirm" ).dialog({
      resizable: false,
      height:180,
      modal: true,
      buttons: {
        "Login": function() {
          $( this ).dialog( "close" );
          location.href = '/accounts/login/';          
        },
        Cancel: function() {
          $( this ).dialog( "close" );
          return false;
        }
      }
    }); 
  }  
  return true;
}

function save_search(e, form_id, logged_in, receive_email) {
  if (!login_check(e, logged_in))
    return false;

    $.post('/residential/save_search/', $('#'+form_id).serialize()+'&form_id='+form_id+'&receive_email='+receive_email)
    .success(function(result){
      console.log('Search is saved successfully!');
    });
}

function profile_save_search(e) {
  receive_email = $('#userprofile-ss-propemail-0').attr('checked');
  if (receive_email != 'checked')
    receive_email = 'unchecked';
  
  save_search(e, 'rent_form', true, receive_email);
  save_search(e, 'sale_form', true);
  save_search(e, 'crent_form', true);
  save_search(e, 'csale_form', true);
}

function toggle_favorite(e, obj, id, logged_in, flag_profile)
{
  var flag = false;
  if (!login_check(e, logged_in))
    return false;

  if (flag_profile) {
    $( "#fav-dialog-confirm" ).dialog({
      resizable: false,
      height:180,
      modal: true,
      buttons: {
        "Delete": function() {
          $( this ).dialog( "close" );
          e.stopPropagation();     
        },
        Cancel: function() {
          $( this ).dialog( "close" );
          return false;
        }
      }
    }); 
  }

  img = $(obj).attr('src');
  if (img == '/static/img/d_star.png') {
    $('.favorite_star.star'+id).attr('src', '/static/img/e_star.png');
    $('#favor_msg').html('This property has been added to your favourites. ');

    $.post('/residential/favorite/', {'id': id, 'operation':1})
    .success(function(result){
      console.log('Favorite added @@@');
    });

  } else {
    $('.favorite_star.star'+id).attr('src', '/static/img/d_star.png');
    $('#favor_msg').html('This property has been removed from your favourites.');

    $.post('/residential/favorite/', {'id': id, 'operation':0})
    .success(function(result){
      console.log('Favorite removed ###');
    });
  }

  if(flag == true) {
    location.href = '/profile/#favorites_profile';
    location.reload();
  }
}
