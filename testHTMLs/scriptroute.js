function displayRoute(startLatitude, startLongitude, endLatitude, endLongitude, waypointsToAvoid) {
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

  // Add pushpins to the avoid coordinates
  waypointsToAvoid.forEach(waypoint => {
    const waypointLocation = new Microsoft.Maps.Location(waypoint.latitude, waypoint.longitude);
    const waypointPin = new Microsoft.Maps.Pushpin(waypointLocation, {
      title: 'Avoid Point'
    });
    map.entities.push(waypointPin);
  });



  map.entities.push(startPin);
  map.entities.push(endPin);

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
  });
}

window.onload = function() {
  // Example start and end coordinates
  const startLatitude = 49.269802;
  const startLongitude = -123.083763;
  const endLatitude = 49.249896;
  const endLongitude = -122.966601;

  // Example waypoints to avoid (can be empty or null if none)
  const waypointsToAvoid = [
    { latitude: 48.0, longitude: -123.0 },
    { latitude: 48.5, longitude: -123.5 },
    { latitude: 48.472762, longitude: -122.342356 },
  ];

  // Call displayRoute with the provided coordinates and waypoints to avoid
  displayRoute(startLatitude, startLongitude, endLatitude, endLongitude, waypointsToAvoid);
};
