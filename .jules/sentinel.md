## 2026-10-09 - Fix XSS in Angular direct DOM manipulation
**Vulnerability:** Raw DOM manipulation (assigning to innerHTML) in ChartTooltip bypasses Angular's built-in DomSanitizer, creating a Cross-Site Scripting (XSS) vulnerability if tooltip data is user-controlled.
**Learning:** Angular only sanitizes bindings like [innerHTML]. Manual DOM manipulation via element.innerHTML = ... is unprotected and requires manual escaping.
**Prevention:** Always manually escape data (e.g., using _.escape from lodash) before direct assignment to innerHTML when bypassing Angular's template binding.
