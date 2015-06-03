function initialize() {

  var scriptPram = document.getElementById('map_canvas');
  var state = scriptPram.getAttribute('state');
  if (state === 'None') {
      state = '';
  }
  console.log(state);
  var city = scriptPram.getAttribute('city');
  if (city === 'None') {
      city = '';
  }
  console.log(city);

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
  var target_url = 'data/get_json?city=' + city + '&state=' + state;
    console.log(target_url);
  xobj.open('GET', target_url, true);
  xobj.onreadystatechange = function () {
      var total_lat = 0;
      var total_lng = 0;
      if (xobj.readyState == 4) {
          var jsonTexto = xobj.responseText;
          var list_from_json = JSON.parse( jsonTexto );
          console.log(list_from_json[0]);

          for(var i=0; i<list_from_json.length; i++) {
              var letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i];
              total_lat += list_from_json[i]['lat'];
              total_lng += list_from_json[i]['lng'];
              var icon_url;
              if (i < 20) {
                  icon_url = "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=" + (i+1) + "|FF0000|000000";
              } else {
                  icon_url = "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|FE7569";
              }
              if (list_from_json[i]['lat'] != 0 || list_from_json[i]['lng']) {
                  console.log(list_from_json[i]['lat']);
                  console.log(list_from_json[i]['lng']);
                  var marker = new google.maps.Marker({
                      position: new google.maps.LatLng(list_from_json[i]['lat'], list_from_json[i]['lng']),
                      map: map,
                      title: 'tooltip text',
                      icon: icon_url
                  });
              }
              /*
              google.maps.event.addListener(marker, 'click', function () {
                var infowindow = new google.maps.InfoWindow({ content: 'hospital info' });
                infowindow.open(map, marker);
              });
              */
          }
      }
      var center_lat = total_lat / list_from_json.length;
      var center_lng = total_lng / list_from_json.length;
      map.setCenter(new google.maps.LatLng(center_lat, center_lng));
};
  xobj.send(null);

}
google.maps.event.addDomListener(window, 'load', initialize);