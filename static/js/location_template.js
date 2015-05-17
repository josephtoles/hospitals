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

  console.log('mark 1');
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/json");
  xobj.open('GET', 'data/get_json', true);
  console.log('mark 2');
  xobj.onreadystatechange = function () {
      console.log('mark 2.5');
      if (xobj.readyState == 4) {
          var jsonTexto = xobj.responseText;
          var list_from_json = JSON.parse( jsonTexto );
          console.log(list_from_json[0]);

          for(var i=0; i<list_from_json.length; i++) {
              var marker = new google.maps.Marker({
                  position: new google.maps.LatLng(list_from_json[i]['lat'], list_from_json[i]['lng']),
                  map: map,
                  title: list_from_json[i]['title']
              });
          }
      }
  };
  xobj.send(null);
  console.log('mark 3');

}
google.maps.event.addDomListener(window, 'load', initialize);