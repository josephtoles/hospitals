function initialize() {

  var myOptions = {
    zoom:8,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

  var siberia = new google.maps.LatLng(37.625364,-122.423905);
  /*

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
  */

  /*
  var mapLabel = new google.maps.MapLabel({
         text: 'Test',
         position: new google.maps.LatLng(50,50),
         map: map,
         fontSize: 20,
         align: 'right'
  });
  */

  map.setCenter(siberia);
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/json");
  xobj.open('GET', 'data/get_json', true);
  xobj.onreadystatechange = function () {
      if (xobj.readyState == 4) {
          var jsonTexto = xobj.responseText;
          var list_from_json = JSON.parse( jsonTexto );
          console.log(list_from_json[0]);

          for(var i=0; i<list_from_json.length; i++) {
              var letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i];
              var marker = new google.maps.Marker({
                  position: new google.maps.LatLng(list_from_json[i]['lat'], list_from_json[i]['lng']),
                  map: map,
                  title: 'tooltip text',
                  icon: "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=" + i + "|FF0000|000000"
              });
              /*
              google.maps.event.addListener(marker, 'click', function () {
                var infowindow = new google.maps.InfoWindow({ content: 'hospital info' });
                infowindow.open(map, marker);
              });
              */
          }

      }
  };
  xobj.send(null);

}
google.maps.event.addDomListener(window, 'load', initialize);