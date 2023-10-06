const age = document.getElementById('age');

fetch('/api/users/')
    .then(response => response.json())
    .then(data => {
        const ageCounts = {}; // Create an object to store age counts

        // Loop to count ages
        data.forEach(user => {
            const age = user.edad; // Get the age from the user data
            if (ageCounts[age]) {
                ageCounts[age]++;
            } else {
                ageCounts[age] = 1;
            }
        });

        const ages = Object.keys(ageCounts); // Get unique ages as labels
        const ageValues = ages.map(age => ageCounts[age]); // Get count values

        new Chart(age, {
            type: 'bar',
            data: {
                labels: ages,
                datasets: [{
                    label: 'Edad',
                    data: ageValues,
                    borderWidth: 2
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
