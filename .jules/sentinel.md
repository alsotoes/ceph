## 2024-06-11 - XSS Vulnerability in Angular via innerHTML
**Vulnerability:** Found unsanitized strings being concatenated into an HTML string and directly assigned to an element's `innerHTML` in `src/pybind/mgr/dashboard/frontend/src/app/shared/models/chart-tooltip.ts`.
**Learning:** Directly assigning to `innerHTML` in Angular bypasses the built-in `DomSanitizer`, making the application vulnerable to Cross-Site Scripting (XSS) if the assigned content is attacker-controlled.
**Prevention:** Always sanitize or escape user-controlled data (e.g., using `_.escape()`) when dynamically constructing HTML strings that will be directly injected into the DOM via `innerHTML` or similar DOM manipulation mechanisms.
