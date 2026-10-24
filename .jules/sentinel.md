## 2024-10-24 - [XSS in ChartTooltip innerHTML]
**Vulnerability:** Raw DOM manipulation via `innerHTML` bypassed Angular's `DomSanitizer`, exposing user-controlled data to Cross-Site Scripting (XSS).
**Learning:** In Angular frontends, direct assignments to `.innerHTML` on elements using vanilla JavaScript bypass built-in XSS protections.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before direct DOM assignment, or use Angular's data-binding and sanitization mechanisms.
