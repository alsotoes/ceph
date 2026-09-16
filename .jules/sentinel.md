## 2024-05-15 - XSS vulnerability in chart tooltip due to innerHTML
**Vulnerability:** A cross-site scripting (XSS) vulnerability was found in the `ChartTooltip` model where chart tooltips dynamically inject unfiltered input (body and title of tooltips) directly into the DOM using `tableRoot.innerHTML = innerHtml;`.
**Learning:** Raw DOM manipulation like `innerHTML` completely bypasses Angular's built-in `DomSanitizer` protections, leading to XSS vulnerabilities. Even fields that seem innocuous like chart tooltips could become an attack vector if data is user-controlled.
**Prevention:** Always sanitize data manually using `_.escape()` from `lodash` (or an equivalent HTML escaping utility) before assigning it directly to `innerHTML` when raw DOM manipulation is unavoidable.
