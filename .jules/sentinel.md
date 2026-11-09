## 2026-11-09 - Prevent XSS in ChartTooltip
**Vulnerability:** Raw string concatenation was used with `.innerHTML` for tooltip generation in `chart-tooltip.ts`.
**Learning:** Bypassing Angular's `DomSanitizer` via `.innerHTML` directly creates XSS vulnerabilities if variables are not properly escaped.
**Prevention:** Always escape variables inserted into raw DOM strings using libraries like `lodash`'s `_.escape()`.
