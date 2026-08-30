## 2024-05-15 - [XSS via raw innerHTML assignment in Angular]
**Vulnerability:** Raw string concatenation into `innerHTML` properties circumvents Angular's `DomSanitizer`, exposing applications to Cross-Site Scripting (XSS) if user input is rendered. Found this in `chart-tooltip.ts` where tooltip contents were constructed by string concatenation.
**Learning:** `DomSanitizer` only partially protects against XSS in innerHTML bindings when you inject data that has been dynamically constructed as an HTML string rather than treating them as separate variables.
**Prevention:** Explicitly sanitize inputs with a library like `lodash` (using `_.escape()`) before dynamically concatenating them into HTML strings intended for `innerHTML` rendering.
