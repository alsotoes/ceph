## 2026-10-31 - ChartTooltip innerHTML XSS Vulnerability
**Vulnerability:** Untrusted input from chart tooltips (title and body) was being injected into the DOM directly using `innerHTML` without sanitization.
**Learning:** Angular's DomSanitizer doesn't fully protect direct assignment to `innerHTML` via raw DOM manipulation on ElementRef in custom implementation logic.
**Prevention:** Always use `_.escape` from lodash or similar sanitization prior to appending data into html strings destined for `innerHTML`.
