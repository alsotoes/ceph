## 2024-05-18 - XSS in Angular via raw DOM manipulation
**Vulnerability:** Found a Cross-Site Scripting (XSS) vulnerability in the Angular frontend (`chart-tooltip.ts`). The code was concatenating user-controlled strings (chart tooltip titles and bodies) into an HTML string, which was then directly assigned to an element's `.innerHTML`.
**Learning:** Raw DOM manipulation (like `element.innerHTML = ...`) bypasses Angular's built-in `DomSanitizer`. Angular only sanitizes data bound via templates (e.g., `[innerHTML]="data"`).
**Prevention:** When manipulating the DOM directly and setting inner HTML, always manually escape the data (e.g., using `lodash.escape`) before appending it to the HTML string.
