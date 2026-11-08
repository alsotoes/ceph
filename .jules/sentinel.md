## 2026-11-08 - Prevent XSS in ChartJS Tooltip
**Vulnerability:** Raw DOM manipulation via `innerHTML` bypassed Angular's DomSanitizer in `ChartTooltip`, exposing the app to Cross-Site Scripting (XSS).
**Learning:** Directly setting `innerHTML` in custom elements like ChartJS tooltips requires explicit sanitization as Angular does not automatically protect these paths.
**Prevention:** Always escape untrusted data using `_.escape` or Angular's `DomSanitizer` before appending it to the DOM.
