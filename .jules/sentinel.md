## 2025-02-23 - DOM Manipulation XSS
**Vulnerability:** Raw DOM manipulation via `innerHTML` without escaping user input in chart tooltips.
**Learning:** Raw DOM manipulation (e.g., direct assignments to `.innerHTML`) bypasses Angular's `DomSanitizer`.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before direct assignment to `innerHTML`.
