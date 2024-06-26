const usuariopcfinal = document.getElementById('usuariopcfinal');
const userpcfinal = document.getElementById('datos');
const idpcfinal = userpcfinal.getAttribute('data-id');

const apiUrl3 = '/api/calculo4';

const datospcfinales = {
  usuarioID_id: idpcfinal,
};

fetch(apiUrl3, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(datospcfinales),
})
  .then((respuesta) => respuesta.json())
  .then((responseDatos) => {
    createRadarChart(usuariopcfinal, responseDatos);
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
