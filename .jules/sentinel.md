## 2024-05-24 - Fix XSS in Angular DOM Manipulation
**Vulnerability:** XSS vulnerability in chart-tooltip.ts where unsanitized user input was assigned directly to `.innerHTML`, bypassing Angular's DomSanitizer.
**Learning:** Even in Angular applications, raw DOM manipulation via `.innerHTML` bypasses built-in XSS protections. Native DOM assignments must be manually sanitized.
**Prevention:** Always use `_.escape()` or a dedicated sanitizer when assigning dynamic data directly to DOM properties like `.innerHTML`, or avoid raw DOM manipulation altogether.
