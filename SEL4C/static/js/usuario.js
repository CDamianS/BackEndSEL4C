const usuario = document.getElementById('usuario'); // Utiliza 'usuario' para el segundo gráfico
const element = document.getElementById('data'); // Utiliza 'data' para el segundo gráfico
const usuarioID = element.getAttribute('data-id');

const apiUrl = '/api/calculo';

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
    createRadarChart(usuario, responseData); // Utiliza 'usuario' para el segundo gráfico
  })
  .catch((error) => {
    console.error('Error al obtener los datos:', error);
});

function createRadarChart(element, data) {
  const labels = Object.keys(data);
  const values = Object.values(data);

  const config = {
    type: 'radar',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Puntuación',
          data: values,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
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

  new Chart(element, config);
}
