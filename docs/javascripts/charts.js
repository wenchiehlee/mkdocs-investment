document$.subscribe(function() {
    console.log("charts.js: document$.subscribe triggered");
    
    var chartContainers = document.querySelectorAll('.margin-chart');
    console.log("charts.js: Found " + chartContainers.length + " chart containers");

    chartContainers.forEach(function(container) {
        var jsonUrl = container.getAttribute('data-url');
        var chartTitle = container.getAttribute('data-title') || '融資餘額分析';
        var chartId = 'chart-' + Math.random().toString(36).substr(2, 9);
        container.id = chartId;

        if (jsonUrl) {
            fetch(jsonUrl)
                .then(response => {
                    if (!response.ok) throw new Error("HTTP error " + response.status);
                    return response.json();
                })
                .then(data => {
                    renderMultiSeriesChart(chartId, data, chartTitle);
                })
                .catch(error => console.error('charts.js: Error loading chart data:', error));
        }
    });

    function renderMultiSeriesChart(elementId, data, title) {
        if (typeof ApexCharts === 'undefined') {
            console.error("charts.js: ApexCharts library not loaded!");
            return;
        }

        // Prepare Series
        var series = [];
        var yaxis = [];
        var colors = ['#000000', '#FFD700', '#FF4560']; // Black, Gold, Red

        // 1. Closing Price (Line)
        if (data.closing_price) {
            var priceData = data.closing_price.sort((a, b) => a[0] - b[0]);
            series.push({
                name: '收盤價 (元)',
                type: 'line',
                data: priceData
            });
            yaxis.push({
                seriesName: '收盤價 (元)',
                axisTicks: { show: true },
                axisBorder: { show: true, color: '#000000' },
                labels: { style: { colors: '#000000' }, formatter: (val) => val.toFixed(1) },
                title: { text: "收盤價 (元)", style: { color: '#000000' } }
            });
        }

        // 2. Margin Balance (Area)
        if (data.margin_balance) {
            var balanceData = data.margin_balance.sort((a, b) => a[0] - b[0]);
            series.push({
                name: '融資餘額 (億)',
                type: 'area',
                data: balanceData
            });
            yaxis.push({
                seriesName: '融資餘額 (億)',
                opposite: true,
                axisTicks: { show: true },
                axisBorder: { show: true, color: '#FFD700' },
                labels: { style: { colors: '#DAA520' }, formatter: (val) => val.toFixed(1) },
                title: { text: "融資餘額 (億)", style: { color: '#DAA520' } }
            });
        }

        // 3. Margin Ratio (Line)
        if (data.margin_ratio) {
            var ratioData = data.margin_ratio.sort((a, b) => a[0] - b[0]);
            series.push({
                name: '融資比率 (%)',
                type: 'line',
                data: ratioData
            });
            yaxis.push({
                seriesName: '融資比率 (%)',
                opposite: true,
                axisTicks: { show: true },
                axisBorder: { show: true, color: '#FF4560' },
                labels: { style: { colors: '#FF4560' }, formatter: (val) => val.toFixed(2) + '%' },
                title: { text: "融資比率 (%)", style: { color: '#FF4560' } }
            });
        }

        var options = {
            series: series,
            chart: {
                id: elementId + '-chart',
                type: 'line', // Base type
                height: 450,
                stacked: false,
                zoom: { autoScaleYaxis: true },
                toolbar: { show: true }
            },
            stroke: { width: [3, 0, 2], curve: 'smooth' },
            colors: colors,
            fill: {
                type: ['solid', 'gradient', 'solid'],
                gradient: {
                    inverseColors: false,
                    shade: 'light',
                    type: "vertical",
                    opacityFrom: 0.85,
                    opacityTo: 0.55,
                    stops: [0, 100, 100, 100]
                }
            },
            markers: { size: 0 },
            xaxis: { type: 'datetime' },
            yaxis: yaxis,
            tooltip: {
                shared: true,
                intersect: false,
                x: { format: 'yyyy-MM-dd' }
            },
            legend: { horizontalAlign: 'left', offsetX: 40 },
            title: { text: title, align: 'center' }
        };

        var container = document.querySelector("#" + elementId);
        if (!container) return;

        // Toolbar
        var toolbar = document.createElement('div');
        toolbar.style.textAlign = 'right';
        toolbar.style.marginBottom = '10px';
        
        var ranges = [
            { label: '1M', days: 30 }, { label: '3M', days: 90 }, { label: '6M', days: 180 },
            { label: '1Y', days: 365 }, { label: '3Y', days: 365 * 3 }, { label: 'All', days: 0 }
        ];

        ranges.forEach(range => {
            var btn = document.createElement('button');
            btn.innerText = range.label;
            btn.className = 'md-button md-button--primary';
            btn.style.marginLeft = '5px';
            btn.style.fontSize = '0.7rem';
            btn.style.padding = '2px 6px';
            btn.onclick = () => {
                var allData = series[0].data;
                var maxDate = allData[allData.length - 1][0];
                var minDate = range.days > 0 ? maxDate - (range.days * 24 * 60 * 60 * 1000) : allData[0][0];
                ApexCharts.exec(elementId + '-chart', 'zoomX', minDate, maxDate);
            };
            toolbar.appendChild(btn);
        });

        container.appendChild(toolbar);
        var chartDiv = document.createElement('div');
        container.appendChild(chartDiv);
        new ApexCharts(chartDiv, options).render();
    }
});
