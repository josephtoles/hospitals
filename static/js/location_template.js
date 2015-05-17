var siberia = new google.maps.LatLng(37.625364,-122.423905);
var siberia2 = new google.maps.LatLng(38.625364,-123.423905);

function initialize() {
  var myOptions = {
    zoom:19,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

  var marker =  new google.maps.Marker({
    position: siberia,
    map: map,
    title: "omt"
  });

  var infowindow = new google.maps.InfoWindow({
      content: "some info for the window"
  });

  google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map,marker);
  });

  var marker2 =  new google.maps.Marker({
    position: siberia2,
    map: map,
    title: "omt"
  });
  map.setCenter(siberia);

}
  google.maps.event.addDomListener(window, 'load', initialize);