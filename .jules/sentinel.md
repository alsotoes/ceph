## 2026-10-03 - DOM-based XSS vulnerability in ChartTooltip
**Vulnerability:** DOM-based XSS via unsanitized ChartJS tooltip payload injected into innerHTML bypassing Angular Sanitizer.
**Learning:** Direct assignments to `.innerHTML` in Angular bypass `DomSanitizer`.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before direct `.innerHTML` assignment.
