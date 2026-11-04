## 2026-11-04 - DOM XSS in Chart Tooltip

**Vulnerability:** Setting `.innerHTML` dynamically without escaping the text first in `ChartTooltip` class allows execution of untrusted scripts.
**Learning:** Directly assigning arbitrary strings to DOM element `.innerHTML` bypasses Angular's DOM Sanitizer, leaving the app open to Cross-Site Scripting (XSS).
**Prevention:** Sanitize the variables (using lodash's `_.escape`) before inserting them into string concatenation, or preferably, use DOM element creation methods (`document.createElement()`) and set `.textContent`.
