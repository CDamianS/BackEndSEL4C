const usuariofinal = document.getElementById('usuariofinal'); // Utiliza 'usuariofinal' para el primer gráfico
const elementfinal = document.getElementById('data'); // Utiliza 'datafinal' para el primer gráfico
const usuarioIDfinal = elementfinal.getAttribute('data-id');

const apiUrlfinal = '/api/calculo3';

const datafinal = {
  usuarioID_id: usuarioIDfinal,
};

fetch(apiUrlfinal, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(datafinal),
})
  .then((response) => response.json())
  .then((responseData) => {
    createRadarChart(usuariofinal, responseData); // Utiliza 'usuariofinal' para el primer gráfico
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
