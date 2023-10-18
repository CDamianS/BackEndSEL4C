const ageChart = document.getElementById('age');
const apiUrl = '/api/users/';

// Función para mapear edades a rangos
function mapAgesToRanges(data) {
    const ageRanges = {
        'Menor a 18': 0,
        '18 a 24': 0,
        '25 a 30': 0,
        'Más de 30': 0
    };

    data.forEach(user => {
        const age = user.edad;

        if (age < 18) {
            ageRanges['Menor a 18']++;
        } else if (age >= 18 && age <= 24) {
            ageRanges['18 a 24']++;
        } else if (age >= 25 && age <= 30) {
            ageRanges['25 a 30']++;
        } else {
            ageRanges['Más de 30']++;
        }
    });

    return ageRanges;
}

// Función para crear el gráfico de rangos de edad
function createAgeChart(data) {
    const ageRanges = mapAgesToRanges(data);
    const ranges = Object.keys(ageRanges);
    const rangeValues = ranges.map(range => ageRanges[range]);

    new Chart(ageChart, {
        type: 'bar',
        data: {
            labels: ranges,
            datasets: [{
                label: 'Rango de Edad',
                data: rangeValues,
                borderWidth: 2
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Rango de Edad de los Usuarios'
                },
                legend: {
                    display: false
                }
            }
        }
    });
}

// Realizar la solicitud a la API
fetch(apiUrl)
    .then(response => response.json())
    .then(data => createAgeChart(data))
    .catch(error => console.error('Error al cargar los datos:', error));
