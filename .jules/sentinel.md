## 2024-05-15 - [XSS vulnerability in chart tooltip]
**Vulnerability:** Direct assignment to `.innerHTML` in `ChartTooltip` bypassing Angular's `DomSanitizer`, leading to XSS.
**Learning:** Raw DOM manipulation escapes Angular's built-in XSS protections. Always sanitize input before assigning to `innerHTML`.
**Prevention:** Use `_.escape()` from lodash to sanitize data before assigning to raw DOM elements.
