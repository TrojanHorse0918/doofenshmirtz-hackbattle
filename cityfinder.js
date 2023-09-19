async function getCityFromLatLng(latitude, longitude) {
    const apiKey = 'Akg2tJWLm6UJu1jjM-aF_OGgQDkJC3xbDV6xgimSckEaBw-ShyHZrWE1MQm0J6o8'; // Replace with your Bing Maps API key
    const apiUrl = `https://dev.virtualearth.net/REST/v1/Locations/${latitude},${longitude}?o=json&key=${apiKey}`;
  
    try {
      const response = await fetch(apiUrl);
      const data = await response.json();
  
      if (data.resourceSets && data.resourceSets.length > 0) {
        const location = data.resourceSets[0].resources[0];
        if (location && location.address && location.address.locality) {
          return location.address.locality; // Return the city
        }
      }
  
      throw new Error('Could not determine city.');
    } catch (error) {
      console.error('Error fetching data:', error);
      throw new Error('Error fetching city data.');
    }
  }
  
//   // Example usage
//   const latitude = 49.269802;
//   const longitude = -123.083763;
  
//   getCityFromLatLng(latitude, longitude)
//     .then(city => console.log('City:', city))
//     .catch(error => console.error('Error:', error));
  