## 2025-01-20 - Prevent XSS in Chart Tooltips via innerHTML
**Vulnerability:** Unsanitized user-controlled data was being assigned directly to the `innerHTML` property of a DOM element, bypassing Angular's built-in DomSanitizer and introducing a Cross-Site Scripting (XSS) vulnerability.
**Learning:** Even within frameworks like Angular, directly manipulating the DOM (such as using `.innerHTML` on native elements) escapes the framework's security context.
**Prevention:** Always sanitize or escape untrusted data before assigning it to `.innerHTML`. Using libraries like lodash `_.escape()` is a reliable way to encode HTML entities when raw text is expected.
