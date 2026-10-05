## 2024-05-24 - XSS via raw DOM manipulation in ChartJS custom tooltip
**Vulnerability:** Raw DOM manipulation via `innerHTML` assignment bypassed Angular's DOMSanitizer in `ChartTooltip`, leading to potential XSS through unescaped title or body text.
**Learning:** In the Angular frontend, raw DOM manipulation (e.g., assigning to `.innerHTML` on elements) completely bypasses Angular's built-in `DomSanitizer`, requiring manual data escaping.
**Prevention:** Always manually escape data (e.g., using `_.escape` from `lodash`) before directly assigning variables to the DOM using `innerHTML`. For lodash imports, use `import * as _ from 'lodash';` to comply with the project's TypeScript configuration.
