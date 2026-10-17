## 2024-10-17 - Prevent XSS in Chart Tooltip innerHTML assignment
**Vulnerability:** XSS vulnerability in ChartJS tooltip where user-controlled tooltip title/body was directly assigned to `innerHTML` without sanitization.
**Learning:** Angular's DomSanitizer doesn't protect against direct `.innerHTML` assignments in components or classes outside Angular's template binding.
**Prevention:** Always escape data using a library like `lodash` (`_.escape`) before directly writing to `.innerHTML`.
