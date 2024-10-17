// Función para obtener el precio de Ethereum desde el servidor

function getEthPrice() {
    // Realiza una solicitud HTTP GET al endpoint '/get_eth_price' para obtener el precio de Ethereum
    fetch('/get_eth_price')
      .then(response => response.json()) // Convierte la respuesta en formato JSON para que pueda ser utilizada
      .then(data => {
        // Si la respuesta contiene el precio de Ethereum, se muestra en el elemento con id 'eth_price'
        if (data.eth_price) {
          document.getElementById('eth_price').innerText = 'Ethereum (ETH): $' + data.eth_price.toFixed(2); // Muestra el precio de Ethereum con dos decimales
        } else {
          // Si no se recibe el precio, muestra un mensaje de error en el elemento con id 'eth_price'
          document.getElementById('eth_price').innerText = 'Error al obtener el precio de Ethereum.';
        }
      })
      .catch(error => {
        // Maneja cualquier error que ocurra durante la solicitud y lo muestra en la consola
        console.error('Error:', error);
        // Muestra un mensaje de error en el elemento con id 'eth_price' si ocurre un problema con la solicitud
        document.getElementById('eth_price').innerText = 'Error al realizar la solicitud.';
      });
  }
  

  
function getBtcPrice() {
  // Realiza una solicitud HTTP GET al endpoint '/get_btc_price' para obtener el precio de Bitcoin
  fetch('/get_btc_price')
    .then(response => response.json()) // Convierte la respuesta en formato JSON para que pueda ser utilizada
    .then(data => {
      // Si la respuesta contiene el precio de Bitcoin, se muestra en el elemento con id 'btc_price'
      if (data.btc_price) {
        document.getElementById('btc_price').innerText = 'Bitcoin (BTC): $' + data.btc_price.toFixed(2); // Muestra el precio de Bitcoin con dos decimales
      } else {
        // Si no se recibe el precio, muestra un mensaje de error en el elemento con id 'btc_price'
        document.getElementById('btc_price').innerText = 'Error al obtener el precio de Bitcoin.';
      }
    })
    .catch(error => {
      // Maneja cualquier error que ocurra durante la solicitud y lo muestra en la consola
      console.error('Error:', error);
      // Muestra un mensaje de error en el elemento con id 'btc_price' si ocurre un problema con la solicitud
      document.getElementById('btc_price').innerText = 'Error al realizar la solicitud.';
    });
}
