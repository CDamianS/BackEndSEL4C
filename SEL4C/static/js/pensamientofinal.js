const pensamientofinal = document.getElementById('pensamientofinal');

fetch('/api/cuestionario_final/')
  .then(response => response.json())
  .then(data => {
    const valoresEscala = {
      "Totalmente de acuerdo": 5,
      "De acuerdo": 4,
      "Ni en acuerdo ni en desacuerdo": 3,
      "En desacuerdo": 2,
      "Totalmente en desacuerdo": 1
    };

    const dimensiones = {
      'Sistémico': [25, 26, 27, 28, 29, 30],
      'Científico': [31, 32, 33, 34, 35, 36, 37, 38],
      'Crítico': [39, 40, 41, 42, 43, 44],
      'Inovador': [45, 46, 47, 48, 49]
    };

    const promedios = {};

    for (const dimension in dimensiones) {
      const dimensionValues = dimensiones[dimension];
      const total = dimensionValues.reduce((acc, num) => acc + valoresEscala[data.find(item => item.numero === num).respuesta], 0);
      const promedio = total / dimensionValues.length;
      promedios[dimension] = promedio;
    }

    new Chart(pensamientofinal, {
      type: 'radar',
      data: {
        labels: Object.keys(promedios),
        datasets: [{
          label: 'Promedio por Dimensión',
          data: Object.values(promedios),
          backgroundColor: '#2565CEAA',
          borderColor: '#34495EFF',
          borderWidth: 1
        }]
      },
      options: {
        scale: {
          ticks: {
            beginAtZero: true,
              min: 1
          }
        }
      }
    });
  })
  .catch(error => console.error(error));
