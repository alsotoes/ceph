## 2024-05-24 - Cross-Site Scripting (XSS) via raw DOM manipulation

**Vulnerability:** Found a Cross-Site Scripting (XSS) risk in `src/pybind/mgr/dashboard/frontend/src/app/shared/models/chart-tooltip.ts` where chart tooltips (titles and body strings) were being concatenated directly into HTML strings and assigned to an element's `innerHTML` without sanitization.
**Learning:** In the Angular frontend, raw DOM manipulation (like `tableRoot.innerHTML = innerHtml;`) bypasses Angular's built-in `DomSanitizer` which usually protects against XSS in templates.
**Prevention:** Always ensure data is properly escaped (e.g., using `_.escape` from `lodash`) before direct assignment to `innerHTML` or when constructing HTML strings manually outside of Angular templates.
