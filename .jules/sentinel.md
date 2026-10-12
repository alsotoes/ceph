## 2024-10-12 - Cross-Site Scripting (XSS) via DOM manipulation bypass

**Vulnerability:** In `chart-tooltip.ts`, Angular's built-in DomSanitizer protection is bypassed because `tableRoot.innerHTML` is modified using manual DOM assignments instead of Angular's structural directives/templates. Data extracted directly from tooltip strings (`getTitle` and `getBody` outputs) were not explicitly escaped, leading to a Cross-Site Scripting (XSS) vulnerability if tooltip content was tainted with attacker-controlled inputs.

**Learning:** When generating HTML dynamically as a string and injecting it via raw DOM properties (like `innerHTML`), Angular's template security boundaries are completely bypassed.

**Prevention:** Either refactor the code to use Angular's components/templates so the framework handles sanitization natively, or explicitly escape dynamic text via utilities like `_.escape` from `lodash` before it is concatenated into HTML strings that will be injected via `innerHTML`.
