## 2024-05-23 - XSS Vulnerability in Chart Tooltips
**Vulnerability:** Raw DOM manipulation via `innerHTML` in ChartJS custom tooltips bypasses Angular's `DomSanitizer`, leading to XSS vulnerabilities if chart data contains malicious input.
**Learning:** Even when working within Angular, raw assignment to element attributes like `innerHTML` bypassing data binding `[innerHTML]` entirely avoids any built-in security sanitization mechanisms.
**Prevention:** Always use a sanitation function like `_.escape` when manually constructing HTML strings to be inserted into the DOM.
