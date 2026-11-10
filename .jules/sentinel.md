## $(date +%Y-%m-%d) - Direct DOM assignment bypasses Angular Sanitizer
**Vulnerability:** XSS via unescaped chart labels assigned to `innerHTML` directly on native DOM elements.
**Learning:** While Angular's `[innerHTML]` binding uses `DomSanitizer`, assigning directly to a native element's `.innerHTML` (e.g., `tableRoot.innerHTML`) bypasses this protection entirely, creating an XSS vector if the content includes user-controlled strings (like chart labels).
**Prevention:** Always escape data using a library like `lodash`'s `escape` before appending it to strings destined for direct `.innerHTML` assignment.
