document$.subscribe(function() {
    // Find all chart containers
    var chartContainers = document.querySelectorAll('.margin-chart');

    chartContainers.forEach(function(container) {
        var jsonUrl = container.getAttribute('data-url');
        var chartTitle = container.getAttribute('data-title') || 'Chart';
        var chartId = 'chart-' + Math.random().toString(36).substr(2, 9);
        container.id = chartId;

        if (jsonUrl) {
            fetch(jsonUrl)
                .then(response => response.json())
                .then(data => {
                    renderChart(chartId, data, chartTitle);
                })
                .catch(error => console.error('Error loading chart data:', error));
        }
    });

    function renderChart(elementId, data, title) {
        // Data is expected to be [[timestamp, value], ...]
        // Ensure data is sorted by date
        data.sort((a, b) => a[0] - b[0]);

        var options = {
            series: [{
                name: title,
                data: data
            }],
            chart: {
                id: elementId + '-chart',
                type: 'area',
                height: 350,
                zoom: {
                    autoScaleYaxis: true
                }
            },
            dataLabels: {
                enabled: false
            },
            markers: {
                size: 0,
                style: 'hollow',
            },
            title: {
                text: title,
                align: 'left'
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0.7,
                    opacityTo: 0.9,
                    stops: [0, 100]
                }
            },
            xaxis: {
                type: 'datetime',
                tooltip: {
                    enabled: false
                }
            },
            yaxis: {
                labels: {
                    formatter: function (val) {
                        return val.toFixed(0);
                    },
                },
                title: {
                    text: 'Value'
                },
            },
            tooltip: {
                x: {
                    format: 'yyyy-MM-dd'
                }
            }
        };

        // Create Button Container
        var container = document.querySelector("#" + elementId);
        var buttonContainer = document.createElement('div');
        buttonContainer.className = 'chart-toolbar';
        buttonContainer.style.marginBottom = '10px';
        buttonContainer.style.textAlign = 'right';
        
        var ranges = [
            { label: '1M', days: 30 },
            { label: '3M', days: 90 },
            { label: '6M', days: 180 },
            { label: '1Y', days: 365 },
            { label: '3Y', days: 365 * 3 },
            { label: '5Y', days: 365 * 5 },
            { label: 'All', days: 0 }
        ];

        ranges.forEach(function(range) {
            var btn = document.createElement('button');
            btn.innerText = range.label;
            btn.className = 'md-button md-button--primary'; // Use MkDocs Material button style
            btn.style.marginLeft = '5px';
            btn.style.fontSize = '0.8rem';
            btn.style.padding = '2px 8px';
            
            btn.addEventListener('click', function() {
                var maxDate = data[data.length - 1][0];
                var minDate = data[0][0];
                
                if (range.days > 0) {
                    var startDate = new Date(maxDate);
                    startDate.setDate(startDate.getDate() - range.days);
                    minDate = startDate.getTime();
                }
                
                ApexCharts.exec(elementId + '-chart', 'zoomX', minDate, maxDate);
            });
            
            buttonContainer.appendChild(btn);
        });

        container.appendChild(buttonContainer);

        // Create chart container div inside the main container to separate it from buttons
        var chartDiv = document.createElement('div');
        container.appendChild(chartDiv);

        var chart = new ApexCharts(chartDiv, options);
        chart.render();
    }
});
