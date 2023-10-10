const usuario_inicial = document.getelementbyid('age');
const usuario_inicial = document.getelementbyid('data');

fetch('/api/users/')
    .then(response => response.json())
    .then(data => {
        const agecounts = {}; // create an object to store age counts

        // loop to count ages
        data.foreach(user => {
            const age = user.edad; // get the age from the user data
            if (agecounts[age]) {
                agecounts[age]++;
            } else {
                agecounts[age] = 1;
            }
        });

        const ages = object.keys(agecounts); // get unique ages as labels
        const agevalues = ages.map(age => agecounts[age]); // get count values

        new chart(age, {
            type: 'bar',
            data: {
                labels: ages,
                datasets: [{
                    label: 'edad',
                    data: agevalues,
                    borderwidth: 2
                }]
            },
            options: {
                scales: {
                    y: {
                        beginatzero: true
                    }
                }
            }
        });
    });
