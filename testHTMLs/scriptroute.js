function displayRoute(startLatitude, startLongitude, endLatitude, endLongitude, hotspots, hospitals, chemists, policeStations, childcare) {
  const map = new Microsoft.Maps.Map(document.getElementById('map'), {
    credentials: 'Akg2tJWLm6UJu1jjM-aF_OGgQDkJC3xbDV6xgimSckEaBw-ShyHZrWE1MQm0J6o8',  // Replace with your actual API key
    center: new Microsoft.Maps.Location(startLatitude, startLongitude),
    zoom: 10
  });

  const startLocation = new Microsoft.Maps.Location(startLatitude, startLongitude);
  const endLocation = new Microsoft.Maps.Location(endLatitude, endLongitude);

  // Add pushpins for start and end points
  const startPin = new Microsoft.Maps.Pushpin(startLocation, {
    title: 'Start Point'
  });

  const endPin = new Microsoft.Maps.Pushpin(endLocation, {
    title: 'End Point'
  });

  map.entities.push(startPin);
  map.entities.push(endPin);

  //Add pins for each hospital in the list
  hospitals.forEach(hospital => {
    const hospitalLocation = new Microsoft.Maps.Location(hospital.latitude, hospital.longitude);
    const hospitalPin = new Microsoft.Maps.Pushpin(hospitalLocation, {
      title: hospital.title,
      iconStyle: 50,
      color: "green"
    });
    map.entities.push(hospitalPin);
  });

  //Add pins for each chemist in the list
  chemists.forEach(chemist => {
    const chemistLocation = new Microsoft.Maps.Location(chemist.latitude, chemist.longitude);
    const chemistPin = new Microsoft.Maps.Pushpin(chemistLocation, {
      title: chemist.title,
      iconStyle: 50,
      color: "yellow"
    });
    map.entities.push(chemistPin);
  });

  //Add pins for each police station in the list
  policeStations.forEach(policeStation => {
    const policeStationLocation = new Microsoft.Maps.Location(policeStation.latitude, policeStation.longitude);
    const policeStationPin = new Microsoft.Maps.Pushpin(policeStationLocation, {
      title: policeStation.title,
      iconStyle: 50,
      color: "blue"
    });
    map.entities.push(policeStationPin);
  });

  //Add pins for each childcare in the list
  childcare.forEach(childcare => {
    const childcareLocation = new Microsoft.Maps.Location(childcare.latitude, childcare.longitude);
    const childcarePin = new Microsoft.Maps.Pushpin(childcareLocation, {
      title: childcare.title,
      iconStyle: 50,
      color: "purple"
    });
    map.entities.push(childcarePin);
  });

  // Add pushpins for each hotspot
  hotspots.forEach(hotspot => {
    const hotspotLocation = new Microsoft.Maps.Location(hotspot.latitude, hotspot.longitude);
    const hotspotPin = new Microsoft.Maps.Pushpin(hotspotLocation, {
      title: hotspot.title,
      color: "red",
      
    });
    map.entities.push(hotspotPin);

  });

  // Calculate the route using Bing Maps REST Services API
  Microsoft.Maps.loadModule('Microsoft.Maps.Directions', function () {
    const directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map);

    const waypointStart = new Microsoft.Maps.Directions.Waypoint({ location: startLocation });
    const waypointEnd = new Microsoft.Maps.Directions.Waypoint({ location: endLocation });

    directionsManager.addWaypoint(waypointStart);
    directionsManager.addWaypoint(waypointEnd);

    directionsManager.setRequestOptions({
      routeMode: Microsoft.Maps.Directions.RouteMode.driving,
      routeDraggable: false,
    });

    directionsManager.setRenderOptions({ itineraryContainer: document.getElementById('itineraryContainer') });
    directionsManager.calculateDirections();
    directionsManager.setActiveRoute(2);
  });
}

window.onload = function() {
  // Example start and end coordinates
  const startLatitude = 49.269802;
  const startLongitude = -123.083763;
  const endLatitude = 49.249546;
  const endLongitude = -123.143682;


  const hotspots = [
    { latitude: 49.280572353951335, longitude: -123.10728217699884, title: 'Crime Hotspot 1' },
    { latitude: 49.26481456376159, longitude: -123.07568646966763, title: 'Crime Hotspot 2' },
    { latitude: 49.21997912962793, longitude: -123.13336347674556, title: 'Crime Hotspot 3' },
    { latitude: 49.23261137517448, longitude: -123.04001459172346, title: 'Crime Hotspot 4' },
    { latitude: 49.27341707144296, longitude: -123.04552540276379, title: 'Crime Hotspot 5' },
    { latitude: 49.26348278114748, longitude: -123.14823048581576, title: 'Crime Hotspot 6' },
    { latitude: 49.224875438523256, longitude: -123.0850877950028, title: 'Crime Hotspot 7' },
    { latitude: 49.258342863786226, longitude: -123.1125414829219, title: 'Crime Hotspot 8' },
    { latitude: 49.28351208457822, longitude: -123.12786437324436, title: 'Crime Hotspot 9' },
    { latitude: 49.25148737246794, longitude: -123.18370978870404, title: 'Crime Hotspot 10' }
  ]

  const hospitals = [
    { latitude: 49.283797, longitude: -123.136465, title: 'Hospital 1' },
    { latitude: 49.269585, longitude: -123.160825, title: 'Hospital 2' },
    { latitude: 49.260557, longitude: -123.122714, title: 'Hospital 3' },
    { latitude: 49.257912, longitude: -123.093218, title: 'Hospital 4' },
  ]

  const chemists = [
    { latitude: 49.2848663, longitude: -123.114852, title: 'Chemist 1' },
    { latitude: 49.2461241, longitude: -123.0676976, title: 'Chemist 2' },
    { latitude: 49.2260355, longitude: -123.090938, title: 'Chemist 3' }
  ]

  const policeStations = [
    { latitude: 49.266381800000005, longitude: -123.11369451517497, title: 'Police Station 1' },
    { latitude: 49.2667629, longitude: -123.08014060464996, title: 'Police Station 2' },
    { latitude: 49.28202425, longitude: -123.09856173429966, title: 'Police Station 3' }
  ]

  const childcare = [
    { latitude: 49.2823497, longitude: -123.0189688, title: 'Childcare 1' },
    { latitude: 49.2795457, longitude: -123.095837, title: 'Childcare 2' },
    { latitude: 49.2313066, longitude: -123.090415, title: 'Childcare 3' }
  ]

  // Call displayRoute with the provided coordinates and waypoints to avoid
  displayRoute(startLatitude, startLongitude, endLatitude, endLongitude, hotspots, hospitals, chemists, policeStations, childcare);
};
