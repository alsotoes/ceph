## 2024-05-24 - Fix XSS in Angular Chart Tooltips
**Vulnerability:** In `ChartTooltip.customTooltips`, direct DOM manipulation using `innerHTML` (`tableRoot.innerHTML = innerHtml`) bypassed Angular's `DomSanitizer`, creating a Cross-Site Scripting (XSS) vulnerability if tooltip titles or body contents contained unsanitized user input.
**Learning:** Raw DOM manipulation bypasses framework security features. Even in frontend code utilizing security features like Angular's DomSanitizer, dynamically created HTML string concatenation assigned to `innerHTML` properties must be explicitly sanitized manually.
**Prevention:** Always escape variables when constructing HTML strings manually for `innerHTML`. Use `_.escape()` from `lodash` to sanitize data before appending it to raw DOM elements.
