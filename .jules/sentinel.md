## 2024-05-24 - Cross-Site Scripting (XSS) via DOM innerHTML assignment
**Vulnerability:** A cross-site scripting vulnerability was found where raw user/chart data might be appended directly into DOM using `.innerHTML` without escaping in Angular.
**Learning:** In the Angular frontend, raw DOM manipulation (e.g., direct assignments to `.innerHTML` on elements) bypasses Angular's `DomSanitizer`.
**Prevention:** Always escape data (e.g., using `_.escape` from `lodash`) before direct assignment. For lodash imports, use `import * as _ from 'lodash';` to comply with the project's TypeScript configuration.
