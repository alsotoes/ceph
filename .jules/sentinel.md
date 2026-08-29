## 2024-05-18 - Fix XSS vulnerability in chart tooltips
**Vulnerability:** XSS vulnerability in chart tooltips due to raw DOM manipulation. The tooltip content was directly inserted using `innerHTML` without proper sanitization.
**Learning:** Angular's `DomSanitizer` does not protect against XSS when using raw DOM manipulation like `innerHTML` assignment. We need to manually sanitize inputs in such cases.
**Prevention:** Use `_.escape` from `lodash` to sanitize the inputs before assigning them to `innerHTML` when using raw DOM manipulation in Angular.
