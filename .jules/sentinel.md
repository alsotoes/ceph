## 2023-10-24 - [Fix XSS in Chart Tooltip innerHTML assignment]
**Vulnerability:** Raw DOM manipulation via `.innerHTML = ...` was used to render chart tooltips, bypassing Angular's `DomSanitizer`, creating an XSS risk.
**Learning:** Even within frameworks that provide automatic sanitization (like Angular), directly modifying DOM elements using `.innerHTML` disables these protections and requires explicit sanitization.
**Prevention:** Always use `_.escape` (or equivalent sanitizers) on external data when performing raw DOM assignments, or prefer framework-native template bindings where sanitization is automatic.
