// TOC Filter - Hide individual stock reports, show only summaries
// This script filters the Table of Contents (TOC) in the right sidebar
// to show only summary reports and hide individual stock reports

document.addEventListener('DOMContentLoaded', function() {
    filterTOC();

    // Re-filter when navigating between pages (for instant navigation)
    document$.subscribe(function() {
        filterTOC();
    });
});

function filterTOC() {
    // Wait a bit for TOC to be fully rendered
    setTimeout(function() {
        const tocItems = document.querySelectorAll('.md-nav--secondary .md-nav__item');

        tocItems.forEach(function(item) {
            const link = item.querySelector('.md-nav__link');
            if (!link) return;

            const text = link.textContent.trim();

            // Pattern to detect individual stock reports:
            // - Contains stock code pattern like (####) where # is a digit
            // - Examples: (2357), (2382), (2412), etc.
            const stockCodePattern = /\(\d{4}\)/;

            // Hide if it matches individual stock report pattern
            if (stockCodePattern.test(text)) {
                item.style.display = 'none';
            }
            // Keep summary reports visible
            // Patterns: "總覽", "Summary", "All Stocks", "所有股票"
            else if (
                text.includes('總覽') ||
                text.includes('Summary') ||
                text.includes('All Stocks') ||
                text.includes('所有股票') ||
                text.includes('Overview')
            ) {
                item.style.display = '';
            }
            // Hide anything else that doesn't match summary patterns
            else {
                // Check if it's a top-level heading (h2) by checking if it has children
                const hasChildren = item.querySelector('.md-nav');
                if (!hasChildren && !text.includes('總覽') && !text.includes('Summary')) {
                    item.style.display = 'none';
                }
            }
        });
    }, 100);
}
