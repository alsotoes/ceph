## 2023-10-24 - Prevent XSS in Angular Component `innerHTML` bindings
**Vulnerability:** Raw DOM manipulation via `innerHTML` on elements bypasses Angular's `DomSanitizer`, exposing the application to XSS vulnerabilities if user data is rendered. In `chart-tooltip.ts`, raw tooltip data was appended to a string and assigned to `innerHTML`.
**Learning:** Angular only automatically sanitizes bindings in templates. When modifying the DOM manually (like setting `innerHTML` in a component or model method), developers must explicitly escape or sanitize data.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before direct assignment to `.innerHTML` in Angular code.
