const general = document.getElementById('general');

fetch('/api/cuestionario_inicial/')
.then(response => response.json())
.then(data => {
    const valoresEscala = {
        "Totalmente de acuerdo": 5,
        "Poco de acuerdo": 4,
        "Ni en acuerdo ni en desacuerdo": 3,
        "Poco en desacuerdo": 2,
        "Totalmente en desacuerdo": 1
    };

    const dimensiones = {
        'Autocontrol': [1, 2, 3, 4],
        'Liderazgo': [5, 6, 7, 8, 9, 10],
        'Conciencia': [11, 12, 13, 14, 15, 16, 17],
        'Innovación': [18, 19, 20, 21, 22, 23, 24]
    };

    const promedios = {};

    for (const dimension in dimensiones) {
        const dimensionValues = dimensiones[dimension];
        const total = dimensionValues.reduce((acc, num) => acc + valoresEscala[data[num]], 0);
        const promedio = total / dimensionValues.length;
        promedios[dimension] = promedio;
    }

    // Configura la gráfica con Chart.js
    new Chart(general, {
        type: 'radar',
        data: {
            labels: Object.keys(promedios),
            datasets: [{
                label: 'Promedio por Dimensión',
                data: Object.values(promedios),
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scale: {
                ticks: { beginAtZero: true, min: 1, max: 5 }
            }
        }
    });
})
.catch(error => console.error(error));