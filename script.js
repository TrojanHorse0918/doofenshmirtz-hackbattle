// Sample latitude and longitude points
const locations = [
    { lat: 49.269802, lng: -123.083763, title: 'Vancouver 1' },
    // Add more locations as needed
  ];
  
  function loadMapScenario() {
    const map = new Microsoft.Maps.Map(document.getElementById('map'), {
      center: new Microsoft.Maps.Location(49.269802, -123.083763),
      zoom: 10
    });
  
    // Add pushpins for each location
    locations.forEach(location => {
      const pin = new Microsoft.Maps.Pushpin(
        new Microsoft.Maps.Location(location.lat, location.lng),
        {
          title: location.title
        }
      );
      map.entities.push(pin);
    });
  }

  window.onload = function() {
    loadMapScenario();
  };
  