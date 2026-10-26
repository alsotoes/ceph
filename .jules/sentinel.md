## 2024-05-15 - [XSS in ChartTooltip]
**Vulnerability:** The `ChartTooltip` class in `src/pybind/mgr/dashboard/frontend/src/app/shared/models/chart-tooltip.ts` assigns an unescaped HTML string to `tableRoot.innerHTML`.
**Learning:** `ChartJS` tooltip custom elements bypass Angular's default HTML sanitization, allowing XSS if the chart labels/titles contain malicious input.
**Prevention:** Use a safe HTML manipulation method or explicitly escape data (e.g. `lodash`'s `escape`) before assigning to `innerHTML`.
