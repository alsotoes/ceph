## 2026-11-11 - XSS via innerHTML DOM Assignment
**Vulnerability:** The ChartTooltip class uses raw `tableRoot.innerHTML` DOM assignment without sanitization. The body strings injected are taken from user/data tooltips directly.
**Learning:** Raw DOM manipulations using `innerHTML` completely bypass Angular's built-in `DomSanitizer`, exposing the application to XSS attacks.
**Prevention:** Always use `_.escape` from lodash (or similar HTML sanitization tools) before directly appending variables to `.innerHTML`.
