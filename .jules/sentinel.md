## 2025-02-09 - [Fix XSS in ChartTooltip innerHTML]
**Vulnerability:** In `src/pybind/mgr/dashboard/frontend/src/app/shared/models/chart-tooltip.ts`, raw strings (title and body from tooltip data) are concatenated into an HTML string which is then injected directly into the DOM using `tableRoot.innerHTML`. This bypasses Angular's DomSanitizer and could lead to Cross-Site Scripting (XSS) if chart data is user-controlled.
**Learning:** Raw DOM manipulation via `innerHTML` bypasses Angular's built-in XSS protection (`DomSanitizer`).
**Prevention:** Always escape variables when constructing HTML strings manually for `innerHTML` assignments using `_.escape()` or similar, or better, use Angular templates binding (`[innerHTML]`) and custom sanitization pipes.
