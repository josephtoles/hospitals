var map;
function initialize() {
  var scriptPram = document.getElementById('map-canvas');
//  var lat = scriptPram.getAttribute('lat');
//  var lng = scriptPram.getAttribute('lng');

//    var l1 = scriptPram.getAttribute('lat');
//    var lng = scriptPram.getAttribute('lng');
  map = new google.maps.Map(document.getElementById('single-hospital-map-canvas'), {
    zoom: 8,
    center: {lat: -34.397, lng: 150.644}
  });
}

google.maps.event.addDomListener(window, 'load', initialize);