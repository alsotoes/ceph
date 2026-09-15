## 2024-05-17 - DOM XSS in Angular Tooltips
**Vulnerability:** Raw DOM manipulation via `innerHTML` assignment bypasses Angular's built-in `DomSanitizer`, creating a Cross-Site Scripting (XSS) vulnerability when user-controlled data is rendered. This was found in `ChartTooltip` string concatenation.
**Learning:** Even within frameworks like Angular that provide automatic contextual sanitization, direct interactions with DOM properties like `innerHTML` completely bypass these protections.
**Prevention:** Always explicitly sanitize or escape data before assigning it to `innerHTML` or similar raw DOM properties. For Angular, use lodash `_.escape` or `DomSanitizer` manually if direct DOM manipulation is unavoidable.
