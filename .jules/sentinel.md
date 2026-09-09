## 2024-05-14 - XSS via innerHTML bypassing Angular DomSanitizer
**Vulnerability:** XSS vulnerability in ChartTooltip class where user-controlled tooltip titles and bodies are directly concatenated and assigned to `innerHTML`.
**Learning:** Raw DOM manipulation using `innerHTML` completely bypasses Angular's built-in `DomSanitizer`, making the application vulnerable to XSS if inputs aren't manually escaped.
**Prevention:** Always use `_.escape` from lodash (or similar) before manually constructing HTML strings to be assigned via `innerHTML`, or avoid `innerHTML` by using Angular's native templates and bindings.
