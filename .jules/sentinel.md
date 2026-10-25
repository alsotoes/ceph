## 2026-10-25 - Prevent XSS in Raw DOM Manipulation (innerHTML)
**Vulnerability:** The ChartTooltip implementation uses raw DOM manipulation (`.innerHTML = innerHtml`) to build a table, bypassing Angular's DomSanitizer and directly concatenating unsanitized text components (title and body).
**Learning:** Even within frameworks like Angular that provide built-in XSS protection, direct DOM manipulation via `ElementRef` and properties like `.innerHTML` can introduce vulnerabilities if the data isn't explicitly sanitized.
**Prevention:** Avoid raw DOM manipulation where possible. When necessary, explicitly escape user-provided data (e.g., using `_.escape()` from lodash) before inserting it into the DOM.
