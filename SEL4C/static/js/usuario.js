const usuario = document.getElementById('usuario');
const usuarioID_id = document.getElementById('data');

fetch("/api/calculo", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ usuarioID_id })
})
.then(response => response.json())
.then(data => {
    // Parsea los datos
    const autocontrol = data.Autocontrol;
    const liderazgo = data.Liderazgo;
    const conciencia = data.Conciencia;
    const innovacion = data.Innovacion;

    // Crea el gráfico
    new Chart(usuario, {
        type: 'radar',
        data: {
            labels: ["Autocontrol", "Liderazgo", "Conciencia", "Innovación"],
            datasets: [{
                data: [autocontrol, liderazgo, conciencia, innovacion],
            }]
        },
        options: {
            scales: {
                r: {
                    min: 0,
                    max: 5,
                    stepSize: 1,
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Respuestas Encuesta Inicial'
                },
                legend: {
                    display: false
                }
            }
        }
    });
})
.catch(error => {
    console.error("Error en la solicitud POST:", error);
});
