## 2024-05-15 - XSS in Chart Tooltip innerHTML assignment
**Vulnerability:** Raw DOM manipulation using `innerHTML` bypasses Angular's DomSanitizer, allowing XSS when constructing tooltips from user-controlled strings.
**Learning:** Using `element.innerHTML` in Angular is dangerous because it bypasses built-in sanitization. Any dynamic data concatenated into HTML strings must be explicitly sanitized.
**Prevention:** Always use `_.escape()` when manually constructing HTML strings, or better, stick to Angular templates (`[innerHTML]`) which auto-sanitize.
