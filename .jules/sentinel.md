## 2024-05-14 - Fix XSS in ChartTooltip innerHTML
**Vulnerability:** Raw DOM manipulation using `.innerHTML` on `tableRoot.innerHTML` in `ChartTooltip` bypassing Angular's DomSanitizer, potentially allowing XSS via unescaped `title` and `body` properties.
**Learning:** Direct assignments to `.innerHTML` in Angular code completely bypass `DomSanitizer`, requiring explicit manual escaping of any user-controlled or dynamically generated data.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before appending it to strings that will be assigned to `.innerHTML`.
