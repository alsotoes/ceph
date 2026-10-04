## 2024-10-04 - XSS via raw DOM manipulation in Angular
**Vulnerability:** Raw DOM manipulation (e.g., direct assignment to `.innerHTML`) in Angular components bypasses the framework's built-in `DomSanitizer`, leading to potential Cross-Site Scripting (XSS) vulnerabilities if untrusted data is injected.
**Learning:** Angular's sanitization only protects against XSS in template bindings (e.g., `[innerHTML]="..."`). Manually constructing HTML strings and assigning them to `element.innerHTML` bypasses this protection.
**Prevention:** Always escape untrusted data (e.g., using `_.escape` from `lodash`) before directly assigning it to `.innerHTML` in raw DOM manipulation, or avoid raw DOM manipulation in favor of Angular's template bindings.
