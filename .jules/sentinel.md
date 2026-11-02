## 2026-11-02 - Fix XSS in ChartTooltip
**Vulnerability:** XSS via unsanitized tooltip strings injected into `innerHTML`.
**Learning:** Directly assigning strings to `innerHTML` bypasses Angular's `DomSanitizer`, requiring manual sanitation for dynamic content like chart tooltips.
**Prevention:** Use `_.escape()` from `lodash` to sanitize any dynamic strings before appending them to `innerHTML`.
