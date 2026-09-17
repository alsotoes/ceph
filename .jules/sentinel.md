## 2024-05-31 - XSS via innerHTML in Angular components
**Vulnerability:** Raw DOM manipulation via `innerHTML` assignment bypasses Angular's built-in `DomSanitizer`, creating a Cross-Site Scripting (XSS) vulnerability.
**Learning:** Even when using Angular, directly assigning data to `innerHTML` or using `el.innerHTML = ...` can lead to XSS if the data isn't properly escaped. Angular's sanitizer only protects property bindings like `[innerHTML]="data"`, and even then, only partially.
**Prevention:** Always escape user-controllable data (e.g., using `_.escape()` from lodash) before concatenating it into HTML strings that will be directly injected into the DOM via `.innerHTML`.
