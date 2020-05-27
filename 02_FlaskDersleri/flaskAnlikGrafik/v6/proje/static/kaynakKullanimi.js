$(document).ready(function () {
    const config = {
        type: 'doughnut',
        data: {
            labels: ['Kullanılan', 'Mevcut'],
            datasets: [{
                label: '# Ram Kullanımı',
                data: [],
                backgroundColor: [
                    '#e74a3b',
                    '#1cc88a',
                ],
                borderColor: [
                    '#ffffff',
                    '#ffffff',
                ]
            }]
        },
        options: {
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'RAM'
            },
            legend: {
                display: false
            },
        }
    };
    
    const context = document.getElementById('ramKullanim').getContext("2d");
    const pieChart = new Chart(context, config);
    const source = new EventSource("/ram");
    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        config.data.datasets[0].data[0] = data['Kullanılan'];
        config.data.datasets[0].data[1] = data['Mevcut'];
        pieChart.update();
    }
});

// https://www.chartjs.org/docs/latest/developers/api.html

$(document).ready(function () {
    const config = {
        type: 'doughnut',
        data: {
            labels: ['Geçerli', 'Maks.'],
            datasets: [{
                label: '# CPU Kullanımı',
                data: [],
                backgroundColor: [
                    '#e74a3b',
                    '#1cc88a',
                ],
                borderColor: [
                    '#ffffff',
                    '#ffffff',
                ]
            }]
        },
        options: {
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'CPU'
            },
            legend: {
                display: false
            },
        }
    };
    
    const context = document.getElementById('cpuKullanimi').getContext("2d");
    const pieChart = new Chart(context, config);
    const source = new EventSource("/cpu");
    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        config.data.datasets[0].data[0] = data['Geçerli'];
        config.data.datasets[0].data[1] = data['Maks.'];
        pieChart.update();
    }
});