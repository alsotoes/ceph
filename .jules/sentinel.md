## 2024-05-15 - High Severity XSS from innerHTML
**Vulnerability:** XSS vulnerability in chart-tooltip.ts via direct innerHTML manipulation without escaping user-controlled chart tooltips.
**Learning:** Using raw DOM assignments like `element.innerHTML = ...` in Angular completely bypasses the built-in `DomSanitizer`, exposing applications to XSS vulnerabilities if the input isn't manually sanitized first.
**Prevention:** Always manually escape strings (e.g. via `lodash.escape()`) when constructing HTML manually and assigning to `.innerHTML`, or avoid it altogether and use Angular's data-binding where possible.
