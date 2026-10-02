## 2024-05-18 - XSS via raw innerHTML assignment in Angular
**Vulnerability:** Raw DOM manipulation via `element.innerHTML` assignment in Angular bypasses the built-in `DomSanitizer`, potentially allowing XSS if untrusted data is injected.
**Learning:** In `src/pybind/mgr/dashboard/frontend/src/app/shared/models/chart-tooltip.ts`, chart tooltips were constructing raw HTML and assigning it to `tableRoot.innerHTML`. Angular's template sanitization doesn't protect raw DOM accesses.
**Prevention:** Always use template binding (e.g., `[innerHTML]="data"`) which goes through Angular's sanitization, or manually escape data using `_.escape()` from `lodash` when direct DOM manipulation is unavoidable.
