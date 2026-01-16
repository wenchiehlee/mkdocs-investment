document$.subscribe(function() {
    console.log("charts.js: document$.subscribe triggered");
    
    // Find all chart containers
    var chartContainers = document.querySelectorAll('.margin-chart');
    console.log("charts.js: Found " + chartContainers.length + " chart containers");

    chartContainers.forEach(function(container) {
        var jsonUrl = container.getAttribute('data-url');
        var chartTitle = container.getAttribute('data-title') || 'Chart';
        var chartId = 'chart-' + Math.random().toString(36).substr(2, 9);
        container.id = chartId;

        console.log("charts.js: Processing container", chartId, "URL:", jsonUrl);

        if (jsonUrl) {
            fetch(jsonUrl)
                .then(response => {
                    console.log("charts.js: Fetch response status:", response.status);
                    if (!response.ok) {
                        throw new Error("HTTP error " + response.status);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log("charts.js: Data received for", chartId, "Type:", typeof data);
                    renderChart(chartId, data, chartTitle);
                })
                .catch(error => console.error('charts.js: Error loading chart data:', error));
        } else {
            console.warn("charts.js: No data-url found for container", container);
        }
    });

    function renderChart(elementId, data, title) {
        console.log("charts.js: renderChart called for", elementId);
        
        // Handle data wrapping (if data is object like {margin_balance: [...]})
        if (!Array.isArray(data)) {
            console.log("charts.js: Data is not an array, checking for wrapped properties...");
            if (data.margin_balance && Array.isArray(data.margin_balance)) {
                console.log("charts.js: Found 'margin_balance' array");
                data = data.margin_balance;
            } else if (data.data && Array.isArray(data.data)) {
                console.log("charts.js: Found 'data' array");
                data = data.data;
            } else {
                console.error('charts.js: Invalid chart data format - could not find array:', data);
                return;
            }
        } else {
            console.log("charts.js: Data is already an array");
        }
        
        if (data.length === 0) {
            console.warn("charts.js: Data array is empty");
            return;
        }

        // Data is expected to be [[timestamp, value], ...]
        // Ensure data is sorted by date
        data.sort((a, b) => a[0] - b[0]);
        console.log("charts.js: Data sorted. Points:", data.length, "First:", data[0], "Last:", data[data.length-1]);

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
                },
                events: {
                    mounted: function (chartContext, config) {
                        console.log("charts.js: ApexChart mounted for", elementId);
                    },
                    updated: function(chartContext, config) {
                        console.log("charts.js: ApexChart updated for", elementId);
                    }
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

        // Check if ApexCharts is loaded
        if (typeof ApexCharts === 'undefined') {
            console.error("charts.js: ApexCharts library not loaded!");
            return;
        }

        // Create Button Container
        var container = document.querySelector("#" + elementId);
        if (!container) {
            console.error("charts.js: Container element not found in DOM:", elementId);
            return;
        }
        
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
                
                console.log("charts.js: Zooming to", new Date(minDate), " - ", new Date(maxDate));
                ApexCharts.exec(elementId + '-chart', 'zoomX', minDate, maxDate);
            });
            
            buttonContainer.appendChild(btn);
        });

        container.appendChild(buttonContainer);

        // Create chart container div inside the main container to separate it from buttons
        var chartDiv = document.createElement('div');
        container.appendChild(chartDiv);

        console.log("charts.js: Initializing ApexCharts instance...");
        var chart = new ApexCharts(chartDiv, options);
        chart.render().then(() => console.log("charts.js: Chart render promise resolved"));
    }
});
