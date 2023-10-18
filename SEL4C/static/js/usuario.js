const usuario = document.getElementById('usuario');
const element = document.getElementById('data');
const usuarioID = element.getAttribute('data-id');

apiUrl = '/api/calculo';

const data = {
  usuarioID_id: usuarioID,
};

fetch(apiUrl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
})
  .then((response) => response.json())
  .then((responseData) => {
    // Crea el gráfico de radar con los datos obtenidos
    createRadarChart(responseData);
  })
  .catch((error) => {
    console.error('Error al obtener los datos:', error);
});

function createRadarChart(data) {
  // Agrega un console.log para verificar los datos recibidos
  console.log(data);  // Utiliza 'data' en lugar de 'responseData'

  const labels = Object.keys(data);  // Obtiene las etiquetas a partir de las claves de los datos
  const values = Object.values(data); // Obtiene los valores a partir de los datos

  // Configuración del gráfico
  const config = {
    type: 'radar',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Puntuación',
          data: values,
          backgroundColor: 'rgba(75, 192, 192, 0.2)', // Color de fondo del gráfico
          borderColor: 'rgba(75, 192, 192, 1)',     // Color del borde del gráfico
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        r: {
          suggestedMin: 0,
          suggestedMax: 5,
        },
      },
    },
  };

  // Crea el gráfico de radar
  new Chart(usuario, config);
}
