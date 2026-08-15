## 2024-05-19 - Avoid Inline Regex Compilation in Loops
**Learning:** Recompiling regexes inside functions that are called frequently (especially in loops, like processing mirroring images) incurs a significant performance penalty compared to compiling them once at the module level.
**Action:** Always move `re.compile()` calls out of functions or loops and define them as module-level constants to ensure they are compiled only once.
