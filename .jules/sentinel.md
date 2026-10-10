## 2024-10-10 - [XSS via raw innerHTML assignment in Angular]
**Vulnerability:** Raw DOM manipulation via `tableRoot.innerHTML = innerHtml;` in `ChartTooltip` bypasses Angular's `DomSanitizer`, causing XSS vulnerabilities if user-provided strings (like chart tooltip bodies or titles) are injected unsanitized.
**Learning:** Angular only automatically sanitizes template bindings (e.g., `[innerHTML]`). If dynamically constructing HTML strings and assigning them directly using native DOM APIs like `innerHTML` in a component or model, the data must be manually sanitized or escaped.
**Prevention:** Always use `_.escape` from `lodash` to sanitize strings before concatenating them into HTML that will be rendered via raw DOM `.innerHTML` assignments.
