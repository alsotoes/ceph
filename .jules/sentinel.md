## 2024-05-24 - XSS vulnerability in ChartTooltip
**Vulnerability:** Raw DOM manipulation via `.innerHTML` bypasses Angular's `DomSanitizer`, exposing the application to Cross-Site Scripting (XSS) if unescaped tooltip data is rendered.
**Learning:** The Angular framework does not sanitize data when assigning directly to `.innerHTML` on elements, necessitating manual escaping.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before direct assignment to `.innerHTML`.
