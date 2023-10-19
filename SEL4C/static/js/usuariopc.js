const usuariopc = document.getElementById('usuariopc');
const user = document.getElementById('datos');
const id = user.getAttribute('data-id');

const apiUrl2 = '/api/calculo2';

const datos = {
  usuarioID_id: id,
};

fetch(apiUrl2, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(datos),
})
  .then((respuesta) => respuesta.json())
  .then((responseDatos) => {
    createRadarChart(usuariopc, responseDatos);
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
