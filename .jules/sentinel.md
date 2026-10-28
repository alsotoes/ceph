## 2024-10-28 - [XSS vulnerability in chart tooltip]
**Vulnerability:** XSS vulnerability in chart tooltips due to unescaped user data directly injected into DOM via .innerHTML.
**Learning:** Raw DOM manipulation bypasses Angular's DomSanitizer, creating potential Cross-Site Scripting (XSS) vulnerabilities.
**Prevention:** Always escape data using `_.escape` from `lodash` before appending it directly to the DOM via .innerHTML.
