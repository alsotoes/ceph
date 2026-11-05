## 2026-11-05 - Prevent XSS in ChartTooltip
**Vulnerability:** XSS vulnerability due to raw strings injected into the DOM innerHTML via `ChartTooltip`.
**Learning:** Using raw innerHTML directly bypasses Angular's built-in `DomSanitizer`, requiring explicit variable escaping with lodash (`_.escape`) prior to insertion into the DOM to mitigate malicious script injection.
**Prevention:** Always escape dynamically generated or untrusted string values before injecting them directly into the DOM (`.innerHTML` properties) by employing a sanitizer module like `_.escape` from lodash.
