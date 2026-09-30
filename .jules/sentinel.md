## 2024-05-30 - Prevent XSS in Chart Tooltips
**Vulnerability:** Raw DOM manipulation via `innerHTML` in `ChartTooltip` bypasses Angular's DOMSanitizer, enabling potential XSS if tooltip contents are not sanitized.
**Learning:** Even internal UI components like custom chart tooltips require sanitization when dynamically rendering strings into the DOM, as Angular's built-in protections only apply to template bindings.
**Prevention:** Always escape dynamic data (e.g. using `_.escape`) before assigning it to `.innerHTML` or `.outerHTML` properties.
