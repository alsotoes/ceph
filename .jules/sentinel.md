## 2024-10-30 - Prevent XSS in ChartJS tooltip
**Vulnerability:** Raw DOM manipulation without escaping user-controlled data was used when rendering the Custom ChartJS Tooltip. `tableRoot.innerHTML = innerHtml` allows injecting potentially malicious HTML or scripts through data objects if properties like tooltip.title or tooltip.body are controlled by the user.
**Learning:** When generating HTML programmatically using template strings or string concatenation to populate `innerHTML`, Angular's default HTML sanitation is completely bypassed.
**Prevention:** Use `_.escape()` from `lodash` to sanitize any dynamic input strings when manually constructing HTML structures assigned to `innerHTML`.
