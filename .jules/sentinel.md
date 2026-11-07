## 2026-11-07 - Fix XSS vulnerability in ChartTooltip via DOM Manipulation
**Vulnerability:** Raw HTML strings constructed via string concatenation and inserted directly using `innerHTML` bypasses Angular's sanitizer. If `title` or `body` properties from `tooltip` come from user input, an XSS vulnerability exists.
**Learning:** Angular's DomSanitizer does not protect against XSS when modifying DOM properties (`innerHTML`) directly on native elements (`ElementRef.nativeElement`).
**Prevention:** Always escape data using `_.escape` from `lodash` before appending it directly to the DOM using `innerHTML`.
