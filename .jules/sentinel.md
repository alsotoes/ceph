## 2026-10-11 - DOM-based XSS via innerHTML in Angular
**Vulnerability:** Raw DOM manipulation (e.g., `.innerHTML = ...`) bypasses Angular's built-in DomSanitizer, leading to XSS if unsanitized data (like chart labels) is used.
**Learning:** Even in frameworks with automatic context-aware escaping (like Angular), directly modifying DOM elements using native properties breaks out of the framework's security boundaries.
**Prevention:** Always escape dynamic data using utilities like `_.escape` when constructing HTML strings for direct DOM assignment, or prefer framework-native template bindings over manual DOM manipulation.
