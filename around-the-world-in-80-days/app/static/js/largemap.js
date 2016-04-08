var map;

var coordinates = {
    "LAX": new google.maps.LatLng(33.941589, -118.408530),
    "BKK": new google.maps.LatLng(13.7563309, 100.50176510000006),
    "LHR": new google.maps.LatLng(51.4700223, -0.4542954999999438),
    "CDG": new google.maps.LatLng(49.009691, 2.547925),
    "SIN": new google.maps.LatLng(1.352083, 103.81983600000001),
    "JFK": new google.maps.LatLng(40.641311, -73.778139),
    "TAV": new google.maps.LatLng(41.00527, 28.976959999999963),
    "DXB": new google.maps.LatLng(25.253175, 55.365673),
    "KUL": new google.maps.LatLng(3.139003, 101.68685499999992),
    "HKG": new google.maps.LatLng(22.308047, 113.918481),
    "BCN": new google.maps.LatLng(41.385064, 2.173403),
    "GMP": new google.maps.LatLng(37.558655, 126.794474),
    "MXP": new google.maps.LatLng(45.630063, 8.725531),
    "CIA": new google.maps.LatLng(15.187910, 120.549405),
    "PVG": new google.maps.LatLng(31.19391, 121.35149100000001),
    "AMS": new google.maps.LatLng(52.3076865, 4.767424099999971),
    "HND": new google.maps.LatLng(35.549393, 139.779839),
    "VIE": new google.maps.LatLng(48.115833, 16.566575000000057),
    "TSA": new google.maps.LatLng(25.067566, 121.55269900000008),
    "RUH": new google.maps.LatLng(24.958202, 46.700779),
    "MEX": new google.maps.LatLng(19.496873, -99.723267),
    "IAD": new google.maps.LatLng(38.953116, -77.456539),
    "LAS": new google.maps.LatLng(36.084000, -115.153739),
    "OGG": new google.maps.LatLng(20.896792, -156.432938),
    "SFO": new google.maps.LatLng(37.621313, -122.378955),
    "PCC": new google.maps.LatLng(1.903117, -75.14532600000001),
    "SYD": new google.maps.LatLng(-33.8674869, 151.20699020000006),
    "GIG": new google.maps.LatLng(-22.9068467, -43.17289649999998),
    "YVR": new google.maps.LatLng(49.196691, -123.181512),
    "EDI": new google.maps.LatLng(55.950785, -3.361453),
    "ZRH": new google.maps.LatLng(47.458216, 8.555476),
    "YUL": new google.maps.LatLng(45.469738, -73.744919)
};

coordinatesList = Object.keys(coordinates).map(function (key) {
    return coordinates[key];
});
centerCity = coordinatesList[Math.floor(Math.random() * coordinatesList.length)]

var MY_MAPTYPE_ID = 'custom_style';

function initialize() {

  var featureOpts = [
    {
      stylers: [
        { saturation: -30 },
        { invert_lightness: false},
        { visibility: 'simplified' },
        { gamma: 0.4 },
        { weight: 0.3 }
      ]
    },
    {
      featureType: 'road',
      elementType: 'labels',
      stylers: [
        { visibility: 'off' }
      ]
    },
    {
      featureType: 'poi.business',
      elementType: 'labels',
      stylers: [
        { visibility: 'off' }
      ]
    }
    // {
    //   elementType: 'water',
    //   stylers: [
    //     { hue: '#000044' }
    //   ]
    //}
  ];


  var mapOptions = {
    zoom: 10,
    mapTypeControlOptions: {
      mapTypeIds: [google.maps.MapTypeId.ROADMAP, MY_MAPTYPE_ID]
    },
    mapTypeId: MY_MAPTYPE_ID
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var styledMapOptions = {
    name: 'Custom Style'
  };

  var customMapType = new google.maps.StyledMapType(featureOpts, styledMapOptions);

  map.mapTypes.set(MY_MAPTYPE_ID, customMapType);
}

google.maps.event.addDomListener(window, 'load', initialize);

google.maps.event.addListener(map, 'zoom_changed', function() {
  var zoomLevel = map.getZoom();
});