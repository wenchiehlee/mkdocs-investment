// DataTables initialization for Stock Analysis System
// Version: 1.0.0
// Purpose: Enable sortable and filterable tables for dividend reports

document$.subscribe(function() {
    // Wait for DOM to be ready
    if (typeof $ === 'undefined' || typeof $.fn.dataTable === 'undefined') {
        console.error('jQuery or DataTables not loaded');
        return;
    }

    // Initialize DataTables for all sortable tables
    $('.sortable-table table').each(function() {
        // Skip if already initialized
        if ($.fn.DataTable.isDataTable(this)) {
            return;
        }

        var $table = $(this);

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

            // Column definitions for better sorting
            columnDefs: [
                {
                    // Stock code column - render Markdown links as HTML
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
                                // Create a safe HTML anchor tag
                                return `<a href="${linkUrl}">${linkText}</a>`;
                            }
                        }
                        return data;
                    }
                },
                {
                    // Numeric columns - auto-detect numbers with % and other symbols
                    targets: '_all',
                    render: function(data, type, row) {
                        if (type === 'sort' || type === 'type') {
                            // Extract numeric value for sorting
                            var num = parseFloat(data.toString().replace(/[^0-9.-]/g, ''));
                            return isNaN(num) ? data : num;
                        }
                        return data;
                    }
                }
            ],

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
