var airportCodes = {
    'New York': 'JFK',
    'Barcelona': 'BCN',
    'Edinburgh': 'EDI',
    'Tokyo': 'HND',
    'Rome': 'CIA',
    'Taipei': 'TSA',
    'Kuala Lumpur': 'KUL',
    'Montreal': 'YUL',
    'Puerto Rico': 'PCC',
    'Bangkok': 'BKK',
    'Singapore': 'SIN',
    'Istanbul': 'TAV',
    'London': 'LHR',
    'Shanghai': 'PVG',
    'Amsterdam': 'AMS',
    'Hong Kong': 'HKG',
    'Vancouver': 'YVR',
    'Washington, D.C.': 'IAD',
    'Rio de Janeiro': 'GIG',
    'Seoul': 'GMP',
    'Zurich': 'ZRH',
    'Riyadh': 'RUH',
    'Paris': 'CDG',
    'Vienna': 'VIE',
    'Sydney': 'SYD',
    'Milan': 'MXP',
    'Dubai': 'DXB',
    'San Francisco': 'SFO',
    'Los Angeles': 'LAX',
    'Maui': 'OGG',
    'Mexico City': 'MEX',
    'Las Vegas': 'LAS'
};
var cities = {
    'JFK': 'New York',
    'BCN': 'Barcelona',
    'EDI': 'Edinburgh',
    'HND': 'Tokyo',
    'CIA': 'Rome',
    'TSA': 'Taipei',
    'KUL': 'Kuala Lumpur',
    'YUL': 'Montreal',
    'PCC': 'Puerto Rico',
    'BKK': 'Bangkok',
    'SIN': 'Singapore',
    'TAV': 'Istanbul',
    'LHR': 'London',
    'PVG': 'Shanghai',
    'AMS': 'Amsterdam',
    'HKG': 'Hong Kong',
    'YVR': 'Vancouver',
    'IAD': 'Washington, D.C.',
    'GIG': 'Rio de Janeiro',
    'GMP': 'Seoul',
    'ZRH': 'Zurich',
    'RUH': 'Riyadh',
    'CDG': 'Paris',
    'VIE': 'Vienna',
    'SYD': 'Sydney',
    'MXP': 'Milan',
    'DXB': 'Dubai',
    'SFO': 'San Francisco',
    'LAX': 'Los Angeles',
    'OGG': 'Maui',
    'MEX': 'Mexico City',
    'LAS': 'Las Vegas'
};
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

function computePath(origin) {
    var xmlhttp = new XMLHttpRequest();
    //var url = "/get_path?origin=" + origin.toString() + "&cities_to_visit=" + document.getElementById("#find").value + "&cities_to_avoid=" + document.getElementById("#avoid").value + "&n_cities=" + document.getElementById("#number").value.toString();
    // var url = "/get_path?origin=" + origin.toString() + "&n_cities=" + document.getElementById("num_cities").value;
    var url = "/get_path?origin=" + origin.toString() + "&n_cities=" + 20;
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var response = JSON.parse(xmlhttp.responseText)["path"];
            var flightPlanCoordinates = [];
            for (var i = 0; i < response.length; i++) {
                console.log(cities[response[i]]);
                flightPlanCoordinates[i] = coordinates[response[i]];
                var marker = new google.maps.Marker({
                    position: coordinates[response[i]],
                    map: map
                });
            }
            var lineSymbol = {
                path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW
            };
            var flightPath = new google.maps.Polyline({
                path: flightPlanCoordinates,
                icons: [{
                    icon: lineSymbol,
                    offset: '100%'
                }],
                geodesic: true,
                strokeColor: '#36C3FF',
                strokeOpacity: 0.9,
                strokeWeight: 1
            });
            flightPath.setMap(map);
            map.setZoom(3);
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function revealMap() {
    // derp
}

function getPathUpdateUI() {
    console.log(document.getElementById("city").value);
    revealMap();
    computePath(airportCodes[document.getElementById("city").value]);
}