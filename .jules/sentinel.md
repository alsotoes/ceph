## 2024-05-24 - Raw DOM Manipulation Bypass
**Vulnerability:** Raw DOM manipulation via `.innerHTML = innerHtml` without escaping user input in Angular applications.
**Learning:** Raw DOM manipulation bypasses Angular's `DomSanitizer`, creating potential XSS vulnerabilities if user data is rendered directly into the HTML string without escaping.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before direct assignment to `.innerHTML`.
