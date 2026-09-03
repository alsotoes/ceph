## 2024-05-24 - Raw DOM Manipulation Bypasses Angular Sanitizer
**Vulnerability:** Raw DOM manipulation like `element.innerHTML = data` bypasses Angular's built-in `DomSanitizer`, leading to potential Cross-Site Scripting (XSS) vulnerabilities if the data contains unsanitized user input.
**Learning:** In `chart-tooltip.ts`, ChartJS tooltip data was being directly injected into a table's `innerHTML`. Even if Angular generally protects against XSS in templates, manual DOM updates in component logic remain vulnerable.
**Prevention:** Always sanitize data before assigning it to `innerHTML` or similar raw DOM properties. For simple text escaping in this codebase, using `lodash`'s `_.escape()` is an effective defense mechanism to ensure malicious scripts are neutralized before rendering.
