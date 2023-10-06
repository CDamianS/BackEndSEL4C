const ctx = document.getElementById('gender');

fetch('/api/users/')
.then(response => response.json())
.then(data => {
    let maleCount = 0;
    let femaleCount = 0;
    let otherCount = 0;
    let noCount = 0;

    // Loop para contar genero
    data.forEach(user => {
        if (user.genero === "Masculino") {
            maleCount++;
        } else if (user.genero === "Femenino") {
            femaleCount++;
        } else if (user.genero === "Otro"){
            otherCount++;
        } else {
            noCount++;
        }
    });
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Masculino', 'Femenino', 'Otro', 'No data'],
            datasets: [{
                label: 'Género',
                data: [maleCount, femaleCount, otherCount, noCount],
                borderWidth: 2
                // borderColor: ['blue', 'pink', 'green']
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
