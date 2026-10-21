## 2024-10-21 - XSS in ChartTooltip `.innerHTML` Assignment
**Vulnerability:** Cross-Site Scripting (XSS) due to raw DOM manipulation. The `chart-tooltip.ts` file assigned unsanitized strings (`this.getTitle(title)` and `this.getBody(body)`) to an element's `.innerHTML` property, bypassing Angular's `DomSanitizer`.
**Learning:** Direct assignments to `.innerHTML` in Angular (or any framework) circumvent built-in sanitization mechanisms, leading to potential XSS if the data originates from user input or external sources.
**Prevention:** Always escape or sanitize data (e.g., using `_.escape` from `lodash` or Angular's `DomSanitizer`) before appending it to the DOM using raw methods like `.innerHTML`.
