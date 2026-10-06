## 2024-05-24 - XSS via raw innerHTML assignment in Angular
**Vulnerability:** Raw string concatenation assigned directly to `.innerHTML` in `ChartTooltip` bypassed Angular's built-in `DomSanitizer`, allowing potential Cross-Site Scripting (XSS) if chart labels/tooltips contained malicious data.
**Learning:** In Angular applications, while template bindings like `[innerHTML]="..."` provide some sanitization, assigning directly to a DOM element's `.innerHTML` property in TypeScript completely bypasses Angular's security mechanisms.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before direct assignment to `.innerHTML`, or rely on Angular's template binding mechanisms with `DomSanitizer` whenever possible.
