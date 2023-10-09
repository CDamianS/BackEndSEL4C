const avance = document.getElementById('avance'); // Cambia el ID del canvas a 'progressChart'

fetch('/api/users/')
    .then(response => response.json())
    .then(data => {
        const progressCounts = [0, 0, 0, 0, 0, 0]; // Inicializa un array para almacenar los recuentos de progreso para cada rango

        // Bucle para contar los valores de progreso
        data.forEach(user => {
            const avance = user.avance; // Obtiene el progreso de los datos del usuario
            if (avance >= 0 && avance <= 5) {
                progressCounts[avance]++;
            }
        });

        const progress = ['0', '1', '2', '3', '4', '5']; // Etiquetas para el eje X
        const progressValues = progressCounts; // Valores de conteo

        new Chart(avance, {
            type: 'line', // Cambia el tipo de gráfico a 'line'
            data: {
                labels: progress,
                datasets: [{
                    label: 'Avance',
                    data: progressValues,
                    borderWidth: 2,
                    borderColor: 'rgba(255, 99, 132, 1)', // Cambia el color de la línea aquí
                    backgroundColor: 'rgba(255, 99, 132, 0.2)', // Cambia el color del área bajo la línea aquí
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });
