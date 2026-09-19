## $(date +%Y-%m-%d) - Raw DOM Manipulation Bypasses Angular Sanitizer
**Vulnerability:** Direct assignment to `.innerHTML` in Angular components using unsanitized user inputs (like chart labels or tooltips) introduces XSS vulnerabilities because it bypasses Angular's built-in `DomSanitizer`.
**Learning:** Even internal formatting functions like `ChartTooltip.customTooltips` that build HTML strings for external libraries (like Chart.js) must be careful when incorporating dynamic strings.
**Prevention:** Always escape dynamic data using utilities like `_.escape` from lodash before appending it to HTML strings that will be assigned via `.innerHTML`.
