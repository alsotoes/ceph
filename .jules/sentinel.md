## 2024-05-15 - [XSS via DOM Manipulation in Angular]
**Vulnerability:** XSS via direct `innerHTML` assignments bypasses Angular's DomSanitizer, leading to XSS vulnerabilities. In `chart-tooltip.ts`, raw tooltip titles and body values were inserted directly into the DOM.
**Learning:** In the Angular frontend, raw DOM manipulation (e.g., direct assignments to `.innerHTML` on elements) bypasses Angular's `DomSanitizer`.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before direct assignment to DOM elements like `innerHTML`. For lodash imports, use `import * as _ from 'lodash';` to comply with the project's TypeScript configuration.
