## 2026-10-29 - XSS in Chart Tooltip
**Vulnerability:** Raw string assignment to `.innerHTML` in `ChartTooltip` bypassing Angular's sanitization, creating an XSS risk when processing chart tooltips.
**Learning:** Raw DOM assignments like `tableRoot.innerHTML = innerHtml` in Angular components circumvent built-in XSS protections (`DomSanitizer`).
**Prevention:** Always sanitize input using `_.escape()` from `lodash` when modifying `.innerHTML` directly.
