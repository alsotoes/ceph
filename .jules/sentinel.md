
## 2024-05-24 - Fix XSS Vulnerability in Chart Tooltips
**Vulnerability:** Cross-Site Scripting (XSS) via unsanitized data assigned to `.innerHTML` in Angular (`ChartTooltip.ts`).
**Learning:** Directly assigning dynamically constructed HTML to `.innerHTML` bypasses Angular's built-in `DomSanitizer`. If the data included in the HTML string contains unsanitized user input, it allows arbitrary script execution.
**Prevention:** Always escape data before direct assignment to `.innerHTML`. When using lodash, use `_.escape()` to sanitize strings, and import it as `import * as _ from 'lodash';` to comply with the project's TypeScript configuration.
