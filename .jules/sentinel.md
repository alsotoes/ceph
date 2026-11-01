## 2026-11-01 - Prevent XSS in Chart Tooltip innerHTML
**Vulnerability:** Raw string variables (title and body) were assigned directly to `.innerHTML` in `chart-tooltip.ts` bypassing Angular's DomSanitizer, creating a Cross-Site Scripting (XSS) vulnerability.
**Learning:** In the Angular frontend, raw DOM manipulation using `.innerHTML` circumvents built-in XSS protections.
**Prevention:** Always sanitize or escape user-provided data using `_.escape` from `lodash` before appending it directly to the DOM when raw DOM manipulation is necessary.
