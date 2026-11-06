
## 2026-11-06 - XSS in ChartTooltip
**Vulnerability:** Raw DOM manipulation via `innerHTML` assignment bypassed Angular's `DomSanitizer` in `ChartTooltip`, leading to potential Cross-Site Scripting (XSS).
**Learning:** Angular's built-in protections do not extend to direct `innerHTML` modifications on native elements like `tableRoot.innerHTML`.
**Prevention:** Always escape dynamic data (e.g., using `_.escape` from `lodash`) before injecting it into the DOM directly.
