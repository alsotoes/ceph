
## 2024-05-15 - [XSS in Angular innerHTML Bypasses DomSanitizer]
**Vulnerability:** User input passed through `ChartTooltip` was concatenated into raw HTML strings and directly assigned to `element.innerHTML`, causing an XSS vulnerability.
**Learning:** While Angular's templates naturally escape interpolated data, manual DOM manipulation (like `element.innerHTML = '...'`) completely bypasses Angular's `DomSanitizer`.
**Prevention:** Always escape data explicitly (e.g. `_.escape(value)`) before interpolating it into raw HTML strings intended for direct DOM assignment via `innerHTML`.
