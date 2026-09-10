## 2024-05-18 - XSS in Chart Tooltips due to Raw DOM Manipulation
**Vulnerability:** Found a Cross-Site Scripting (XSS) vulnerability in `src/pybind/mgr/dashboard/frontend/src/app/shared/models/chart-tooltip.ts` where unescaped string values (`title` and `body`) were assigned directly to a DOM element via `.innerHTML`.
**Learning:** In Angular, raw DOM manipulation (like `element.innerHTML = ...`) bypasses Angular's built-in `DomSanitizer` protections, creating a potential XSS vector if user-controlled data is used.
**Prevention:** Always sanitize or escape user-controlled or dynamic data (e.g., using `_.escape()` from Lodash) before appending it directly to the DOM, or rely on Angular's template binding (`[innerHTML]`) to safely handle rendering.
