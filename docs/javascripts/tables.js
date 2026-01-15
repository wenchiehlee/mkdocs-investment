// DataTables initialization for Stock Analysis System
// Version: 1.0.3
// Purpose: Enable sortable and filterable tables for dividend reports and render emojis in headers

document$.subscribe(function() {
    // Wait for DOM to be ready
    if (typeof $ === 'undefined' || typeof $.fn.dataTable === 'undefined') {
        console.error('jQuery or DataTables not loaded');
        return;
    }

    // Mapping of emoji shortcodes to Unicode characters
    const emojiMap = {
        ':identification_card:': '&#x1f4b3;', // 💳
        ':building_construction:': '&#x1f3d7;&#xfe0f;', // 🏗️
        ':moneybag:': '&#x1f4b0;', // 💰
        ':chart:': '&#x1f4c8;', // 📈
        ':arrow_down:': '&#x2b07;&#xfe0f;', // ⬇️
        ':arrow_up:': '&#x2b06;&#xfe0f;', // ⬆️
        ':repeat:': '&#x1f501;', // 🔁
        ':traffic_light:': '&#x1f6a6;', // 🚥
        ':date:': '&#x1f4c5;', // 📅
        ':calendar:': '&#x1f4c5;', // 📅
        ':money_with_wings:': '&#x1f4b8;', // 💸
        ':chart_with_upwards_trend:': '&#x1f4c8;', // 📈
        ':bar_chart:': '&#x1f4ca;', // 📊
        ':1234:': '&#x1f522;', // 🔢
        ':hourglass:': '⏳', // ⏳ hourglass
        ':clock3:': '🕒', // 🕒 three o'clock
        ':trophy:': '&#x1f3c6;', // 🏆
        ':100:': '&#x1f4af;', // 💯
        ':information_source:': '&#x2139;&#xfe0f;', // ℹ️
        ':crystal_ball:': '&#x1f52e;', // 🔮
        ':star:': '&#x2b50;', // ⭐
        ':seedling:': '&#x1f331;', // 🌱
        ':key:': '&#x1f511;', // 🔑
        ':clipboard:': '&#x1f4cb;', // 📋
        ':new:': '&#x1f195;', // 🆕
        ':two:': '&#x0032;&#xfe0f;&#x20e3;', // 2️⃣
        ':three:': '&#x0033;&#xfe0f;&#x20e3;', // 3️⃣
        ':five:': '&#x0035;&#xfe0f;&#x20e3;', // 5️⃣
        ':keycap_ten:': '&#x1f51f;', // 🔟
        ':factory:': '&#x1f3ed;', // 🏭
        ':left_right_arrow:': '&#x2194;&#xfe0f;' // ↔️
    };

    // Function to replace emoji shortcodes in a given text
    function replaceEmojiShortcodes(text) {
        let newText = text;
        for (const shortcode in emojiMap) {
            newText = newText.replace(new RegExp(shortcode, 'g'), emojiMap[shortcode]);
        }
        return newText;
    }

    // Normalize report links for MkDocs pretty URLs
    function normalizeReportLink(url) {
        let fixedUrl = url;
        const isExternal = /^(https?:)?\/\//.test(fixedUrl);
        if (!isExternal && !fixedUrl.startsWith('../') && !fixedUrl.startsWith('./') && !fixedUrl.startsWith('/')) {
            fixedUrl = '../' + fixedUrl;
        }
        if (/stage2-cleaning-.*\.md$/i.test(fixedUrl)) {
            fixedUrl = fixedUrl.replace(/\.md$/i, '/');
        }
        return fixedUrl;
    }

    // Add 'sortable-table' class to tables within '.annotate' divs that don't already have it
    $('.annotate table:not(.sortable-table)').addClass('sortable-table');
    console.log('Added sortable-table class to tables within .annotate divs that were missing it.');

    // Pre-process table headers to replace emoji shortcodes before DataTables initialization
    $('.sortable-table th').each(function() {
        const $th = $(this);
        $th.html(replaceEmojiShortcodes($th.html()));
    });

    // Pre-process table body cells to replace emoji shortcodes and render Markdown links
    $('.sortable-table td').each(function() {
        const $td = $(this);
        let html = $td.html();

        // Replace emoji shortcodes
        html = replaceEmojiShortcodes(html);

        // Convert Markdown links [**text**](url) to HTML <a> tags
        // Also fix relative paths: add ../ prefix and remove .md extension
        html = html.replace(/\[\*\*(.*?)\*\*\]\((?:\.\.\/)?(stage2-cleaning-.*?)\)/g, function(match, text, url) {
            let fixedUrl = normalizeReportLink(url);
            return '<a href="' + fixedUrl + '"><strong>' + text + '</strong></a>';
        });

        $td.html(html);
    });

    // Helper to extract numeric value from mixed HTML/text
    function parseNumeric(data) {
        var text = $('<div>').html(data).text();
        var cleaned = text.replace(/[^\d.+-]/g, '');
        var num = parseFloat(cleaned);
        return isNaN(num) ? null : num;
    }

    // Helper to convert YYYY/MM strings into sortable numbers
    function parseYearMonth(data) {
        var text = $('<div>').html(data).text().trim();
        var parts = text.split('/');
        if (parts.length === 2) {
            var year = parseInt(parts[0], 10);
            var month = parseInt(parts[1], 10);
            if (!isNaN(year) && !isNaN(month)) {
                return year * 100 + month;
            }
        }
        return null;
    }

    // Helper to convert Market Cap strings (e.g. "1.2 兆元", "500 億元") into sortable numbers
    function parseMarketCap(data) {
        var text = $('<div>').html(data).text().trim();
        // Remove commas
        text = text.replace(/,/g, '');
        
        var val = parseFloat(text);
        if (isNaN(val)) return 0;

        if (text.includes('兆')) {
            return val * 10000; // Convert Trillion to 100 Million unit
        } else if (text.includes('億')) {
            return val;
        } else if (text.includes('萬')) {
            return val / 10000;
        }
        return val;
    }

    // Initialize DataTables for all sortable tables
    $('table.sortable-table').each(function() {
        // Skip if already initialized
        if ($.fn.DataTable.isDataTable(this)) {
            console.log('DataTable already initialized for:', $(this).attr('id') || 'unnamed table');
            return;
        }

        var $table = $(this);
        console.log('Attempting to initialize DataTable for:', $table.attr('id') || 'unnamed table');

        // Detect table type by column count
        var columnCount = $table.find('thead th').length;
        var headerText = $table.find('thead').text();
        console.log('Table has', columnCount, 'columns');

        // Robust detection for Dividend Report: Check header text OR column count
        // The dividend report is distinctively 10 or 12 columns wide.
        var isDividendReport = headerText.includes('現金股利') || columnCount === 10 || columnCount === 12;

        // Build columnDefs based on table type
        var columnDefs = [
            {
                // Stock code column - render Markdown links as HTML (applies to all tables)
                targets: 0,
                type: 'string',
                render: function(data, type, row) {
                    if (type === 'display' || type === 'filter') {
                        // Regex to extract link text and URL from Markdown format [text](url)
                        const markdownLinkRegex = /\[\*\*(.*?)\*\*\]\((.*?)\)/;
                        const match = data.match(markdownLinkRegex);

                        if (match && match.length === 3) {
                            const linkText = match[1];
                            const linkUrl = match[2];
                            const fixedUrl = normalizeReportLink(linkUrl);
                            // Create a safe HTML anchor tag
                            return `<a href="${fixedUrl}">${linkText}</a>`;
                        }
                    }
                    return data;
                }
            }
        ];

        if (headerText.includes('ROE') && headerText.includes('ROA')) {
            // ROA/ROE report
            columnDefs.push({
                // Percentage columns: ROE (col 3), ROA (col 4) - assuming 0-based index
                targets: [3, 4],
                type: 'num',
                render: function(data, type, row) {
                    if (type === 'sort' || type === 'type') {
                        // Use existing percent-pre logic or simple parse
                        return parseFloat(data.replace('%', '')) || 0;
                    }
                    return data;
                }
            });
        } else if (isDividendReport) {
            // Dividend report: Supports both 10-column and 12-column formats
            // Common targets: Code (0), Name (1), Cash Dividend (2)
            var numericTargets = [2];
            var percentageTargets = [];
            var stabilityTarget = -1;
            var timeTarget = -1;

            if (columnCount === 10) {
                // Legacy 10-column format
                percentageTargets = [3, 5, 6, 7]; // Yield@Current, Yield@Low, Yield@High, Payout Ratio
                timeTarget = 4;
                stabilityTarget = 8;
            } else if (columnCount === 12) {
                // New 12-column format (adds 3 prediction columns)
                numericTargets = [2, 3, 4, 5]; // Cash, Predict, TTM Predict, Factset Predict
                percentageTargets = [6, 8, 9, 10]; // Yield@Current, Yield@Low, Yield@High, Payout Ratio
                timeTarget = 7;
                stabilityTarget = 11;
            }

            columnDefs.push({
                targets: numericTargets.concat(percentageTargets),
                type: 'num',
                render: function(data, type, row) {
                    if (type === 'sort' || type === 'type') {
                        var num = parseNumeric(data);
                        return num === null ? 0 : num;
                    }
                    return data;
                }
            });

            if (timeTarget !== -1) {
                columnDefs.push({ targets: [timeTarget], type: 'string' });
            }

            if (stabilityTarget !== -1) {
                columnDefs.push({
                    targets: [stabilityTarget],
                    type: 'num',
                    render: function(data, type, row) {
                        if (type === 'sort' || type === 'type') {
                            var num = parseNumeric(data);
                            return num === null ? 0 : num;
                        }
                        return data;
                    }
                });
            }
        } else if (columnCount === 6) {
            // Revenue report: 6 columns
            columnDefs.push({
                targets: [2, 4],
                type: 'num',
                render: function(data, type, row) {
                    if (type === 'sort' || type === 'type') {
                        var num = parseNumeric(data);
                        return num === null ? 0 : num;
                    }
                    return data;
                }
            });
            columnDefs.push({
                targets: [3],
                type: 'num',
                render: function(data, type, row) {
                    if (type === 'sort' || type === 'type') {
                        var ym = parseYearMonth(data);
                        return ym !== null ? ym : 0;
                    }
                    return data;
                }
            });
        } else if (columnCount === 8) {
            // Margin Daily report: 8 columns (代號, 名稱, 融資餘額, 收盤價, 市值, 比率, 風險, 最新日期)
            columnDefs.push({
                // Numeric columns: 融資餘額 (col 2), 收盤價 (col 3), 比率 (col 5)
                targets: [2, 3, 5],
                type: 'num',
                render: function(data, type, row) {
                    if (type === 'sort' || type === 'type') {
                        var num = parseNumeric(data);
                        return num === null ? 0 : num;
                    }
                    return data;
                }
            });
            columnDefs.push({
                // Market Cap column: 市值 (col 4) - Use custom parser
                targets: [4],
                type: 'num',
                render: function(data, type, row) {
                    if (type === 'sort' || type === 'type') {
                        return parseMarketCap(data);
                    }
                    return data;
                }
            });
        }

        // DataTables configuration
        $table.DataTable({
            // Pagination
            paging: true,
            pageLength: -1,  // Show all items by default
            lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "全部"]],

            // Search/Filter
            searching: true,
            searchDelay: 300,

            // Sorting
            ordering: true,
            order: [], // No default sorting

            // Display
            info: true,
            autoWidth: false,
            responsive: true,

            // Language customization (Traditional Chinese)
            language: {
                "processing": "處理中...",
                "loadingRecords": "載入中...",
                "lengthMenu": "顯示 _MENU_ 筆結果",
                "zeroRecords": "沒有符合的資料",
                "info": "顯示第 _START_ 至 _END_ 筆結果，共 _TOTAL_ 筆",
                "infoEmpty": "顯示第 0 至 0 筆結果，共 0 筆",
                "infoFiltered": "(從 _MAX_ 筆結果中篩選)",
                "search": "搜尋:",
                "paginate": {
                    "first": "第一頁",
                    "previous": "上一頁",
                    "next": "下一頁",
                    "last": "最後一頁"
                },
                "aria": {
                    "sortAscending": ": 升冪排列",
                    "sortDescending": ": 降冪排列"
                }
            },

            // Column definitions (built dynamically based on table type)
            columnDefs: columnDefs,

            // Initialization callback
            initComplete: function(settings, json) {
                console.log('DataTable initialized for:', $table.attr('id') || 'unnamed table');

                // Add custom search placeholder
                $('.dataTables_filter input').attr('placeholder', '輸入關鍵字篩選...');

                // Highlight search terms
                this.api().on('draw', function() {
                    var searchTerm = $('.dataTables_filter input').val();
                    if (searchTerm) {
                        highlightSearchTerms($table, searchTerm);
                    }
                });

                // --- Custom Filter for Dividend Report ---
                if (isDividendReport) {
                    var tableApi = this.api();
                    var $wrapper = $table.closest('.dataTables_wrapper');
                    
                    // Find the index of "殖利率@當日價" dynamically
                    var yieldColIndex = -1;
                    $table.find('thead th').each(function(i) {
                        var text = $(this).text();
                        // Check for "Yield" and "Current" keywords
                        if (text.includes('殖利率') && text.includes('當日')) {
                            yieldColIndex = i;
                        }
                    });

                    if (yieldColIndex !== -1) {
                        // Create filter container
                        var $filterContainer = $('<div class="yield-filter-container" style="margin-bottom: 10px; display: flex; align-items: center; background: var(--md-code-bg-color); padding: 8px; border-radius: 4px;"></div>');
                        var $label = $('<label style="margin-right: 8px; font-weight: bold; color: var(--md-typeset-color);">🔍 篩選 殖利率@當日價 >= </label>');
                        var $input = $('<input type="number" step="0.1" min="0" placeholder="0" style="padding: 4px 8px; border: 1px solid var(--md-typeset-table-color); border-radius: 4px; width: 80px;">');
                        var $suffix = $('<span style="margin-left: 5px; color: var(--md-typeset-color);">%</span>');

                        $filterContainer.append($label).append($input).append($suffix);
                        
                        // Insert before the table controls
                        $wrapper.prepend($filterContainer);

                        // Custom DataTables filtering function
                        $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
                            if (settings.nTable !== $table[0]) {
                                return true;
                            }

                            var minYield = parseFloat($input.val());
                            if (isNaN(minYield) || minYield <= 0) {
                                return true;
                            }

                            var colValueStr = data[yieldColIndex] || "0";
                            var colValue = parseFloat(colValueStr.replace('%', ''));

                            return !isNaN(colValue) && colValue >= minYield;
                        });

                        // Trigger redraw on input change
                        $input.on('keyup change input', function() {
                            tableApi.draw();
                        });
                    }
                }
                // --- Custom Filter for Margin Daily Report (8 columns) ---
                else if (columnCount === 8) {
                    var tableApi = this.api();
                    var $wrapper = $table.closest('.dataTables_wrapper');
                    
                    // Find the index of "比率" dynamically (usually index 5)
                    var ratioColIndex = -1;
                    $table.find('thead th').each(function(i) {
                        if ($(this).text().includes('比率')) {
                            ratioColIndex = i;
                        }
                    });

                    if (ratioColIndex !== -1) {
                        // Create filter container
                        var $filterContainer = $('<div class="margin-filter-container" style="margin-bottom: 10px; display: flex; align-items: center; background: var(--md-code-bg-color); padding: 8px; border-radius: 4px;"></div>');
                        var $label = $('<label style="margin-right: 8px; font-weight: bold; color: var(--md-typeset-color);">🔍 篩選 比率 >= </label>');
                        var $input = $('<input type="number" step="0.1" min="0" placeholder="0" style="padding: 4px 8px; border: 1px solid var(--md-typeset-table-color); border-radius: 4px; width: 80px;">');
                        var $suffix = $('<span style="margin-left: 5px; color: var(--md-typeset-color);">%</span>');

                        $filterContainer.append($label).append($input).append($suffix);
                        
                        // Insert before the table controls
                        $wrapper.prepend($filterContainer);

                        // Custom DataTables filtering function
                        $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
                            if (settings.nTable !== $table[0]) {
                                return true;
                            }

                            var minRatio = parseFloat($input.val());
                            if (isNaN(minRatio) || minRatio <= 0) {
                                return true;
                            }

                            // Parse percentage from "比率" column
                            var colValueStr = data[ratioColIndex] || "0";
                            var colValue = parseFloat(colValueStr.replace('%', ''));

                            return !isNaN(colValue) && colValue >= minRatio;
                        });

                        // Trigger redraw on input change
                        $input.on('keyup change input', function() {
                            tableApi.draw();
                        });
                    }
                }
                // ------------------------------------------
            },

            // Error handling
            error: function(settings, helpPage, message) {
                console.error('DataTables error:', message);
            }
        });
    });

    // Helper function to highlight search terms
    function highlightSearchTerms($table, searchTerm) {
        if (!searchTerm) return;

        $table.find('tbody td').each(function() {
            var $td = $(this);
            var text = $td.text();
            var highlightedText = text.replace(
                new RegExp('(' + escapeRegex(searchTerm) + ')', 'gi'),
                '<mark>$1</mark>'
            );
            if (text !== highlightedText) {
                $td.html(highlightedText);
            }
        });
    }

    // Escape regex special characters
    function escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    // Custom sorting for stock codes (numeric then alphabetic)
    $.fn.dataTable.ext.type.order['stock-code-pre'] = function(data) {
        var code = data.toString().trim();
        return parseInt(code) || code;
    };

    // Custom sorting for percentages
    $.fn.dataTable.ext.type.order['percent-pre'] = function(data) {
        return parseFloat(data.toString().replace('%', '')) || 0;
    };

    // Custom sorting for Chinese text with emoji
    $.fn.dataTable.ext.type.order['chinese-emoji-pre'] = function(data) {
        // Remove emojis for sorting
        return data.toString().replace(/[\u{1F300}-\u{1F9FF}]/gu, '').trim();
    };
});

// Log when script is loaded
console.log('Stock Analysis System - DataTables script loaded');
