## 2024-05-24 - DOM-based XSS via direct innerHTML manipulation
**Vulnerability:** User-controlled chart tooltip data (titles and body) was passed directly into `tableRoot.innerHTML` in `chart-tooltip.ts`.
**Learning:** Raw DOM manipulation, such as assigning directly to `.innerHTML`, bypasses Angular's `DomSanitizer`, creating severe DOM-based XSS vulnerabilities if the input is untrusted or unescaped.
**Prevention:** Always use Angular's built-in binding mechanisms (like `[innerHTML]`) which sanitize data automatically, or explicitly sanitize/escape data (e.g., using `_.escape` from `lodash` or `DOMPurify`) before any raw DOM insertion.
