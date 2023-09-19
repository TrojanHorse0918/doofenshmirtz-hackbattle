function loadMapScenario() {
    console.log("loadMapScenario");
    // Sample latitude and longitude points
    const startPoint = { lat: 37.7749, lng: -122.4194, title: 'Start Point' };
    const endPoint = { lat: 37.3382, lng: -121.8863, title: 'End Point' }; // Sample end point
  const map = new Microsoft.Maps.Map(document.getElementById('map'), {
    center: new Microsoft.Maps.Location(startPoint.lat, startPoint.lng),
    zoom: 10
  });

  // Add pushpins for start and end points
  const startPin = new Microsoft.Maps.Pushpin(
    new Microsoft.Maps.Location(startPoint.lat, startPoint.lng),
    {
      title: startPoint.title
    }
  );

  const endPin = new Microsoft.Maps.Pushpin(
    new Microsoft.Maps.Location(endPoint.lat, endPoint.lng),
    {
      title: endPoint.title
    }
  );

  map.entities.push(startPin);
  map.entities.push(endPin);

  // Create a directions manager
  const directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map);

  // Specify the start and end waypoints for the route
  const startWaypoint = new Microsoft.Maps.Directions.Waypoint({
    location: new Microsoft.Maps.Location(startPoint.lat, startPoint.lng),
    pushpin: startPin
  });

  const endWaypoint = new Microsoft.Maps.Directions.Waypoint({
    location: new Microsoft.Maps.Location(endPoint.lat, endPoint.lng),
    pushpin: endPin
  });

  console.log(startWaypoint);
  console.log(endWaypoint);

  directionsManager.addWaypoint(startWaypoint);
  directionsManager.addWaypoint(endWaypoint);

  // Set the render options for the directions
  const renderOptions = {
    itineraryContainer: document.getElementById('itineraryContainer'),
    waypointPushpinOptions: {
      title: '{index}',
      text: '{index}'
    },
    displayDisclaimer: true,
    displayManeuverIcons: true,
    displayPostItineraryItemHints: true,
    displayRouteSelector: true
  };
  directionsManager.setRenderOptions(renderOptions);

  // Calculate the directions
  directionsManager.calculateDirections();
}

window.onload = function() {
    console.log("window.onload");
    loadMapScenario();
};

