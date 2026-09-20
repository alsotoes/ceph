## 2024-05-24 - XSS in ChartJS Tooltips via innerHTML assignment
**Vulnerability:** The ChartTooltip model manually builds an HTML string containing unescaped chart labels (title and body) and assigns it directly to `element.innerHTML`, which bypasses Angular's DomSanitizer and creates an XSS vulnerability.
**Learning:** Raw DOM manipulation via `innerHTML` in Angular components or services completely bypasses built-in XSS protection (`DomSanitizer`). Data originating from APIs or users must be manually escaped when used in this manner.
**Prevention:** Always use `_.escape` from lodash (or similar HTML escaping utilities) to sanitize any dynamic data before directly assigning it to `.innerHTML`.
