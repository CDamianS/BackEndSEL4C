const general = document.getElementById('general');

var data = {
    labels: ['Autocontrol', 'Liderazgo', 'Conciencia', 'Innovación'],
    datasets: [
        {
            label: 'Promedio de Respuestas',
            data: [2, 4, 3, 4], // Cambia estos valores según tus promedios
            backgroundColor: 'rgba(75, 192, 192, 0.2)', // Color de fondo
            borderColor: 'rgba(75, 192, 192, 1)', // Color del borde
            borderWidth: 2
        }
    ]
};

var miGrafica = new Chart(general, {
    type: 'radar', // Tipo de gráfico radar
    data: data,
    options: {
        scales: {
            r: {
                beginAtZero: true,
                min: 1, // Valor mínimo en el eje radial
                max: 4, // Valor máximo en el eje radial
            }
        }
    }
});
