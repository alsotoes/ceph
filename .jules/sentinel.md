## 2024-05-24 - XSS in Chart Tooltips
**Vulnerability:** Raw DOM manipulation via `innerHTML` in `ChartTooltip` bypassing Angular's `DomSanitizer` allowed potential XSS.
**Learning:** Direct assignments to `innerHTML` outside Angular templates do not automatically sanitize content.
**Prevention:** Always escape data using `_.escape` before direct assignment to `innerHTML`.
