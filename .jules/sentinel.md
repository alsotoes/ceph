## 2024-05-18 - Prevent XML Entity Expansion and XXE Vulnerabilities
**Vulnerability:** Native `xml.etree.ElementTree` in Python is vulnerable to XML Entity Expansion (Billion Laughs) and XXE attacks when parsing untrusted XML data (e.g., from RGW service responses).
**Learning:** Even though Python 3's `xml.etree.ElementTree` does not expand external entities by default, it is still susceptible to billion-laughs attacks. `defusedxml` is required to safely parse untrusted XML.
**Prevention:** Always use `defusedxml.ElementTree` as a drop-in replacement for `xml.etree.ElementTree` when handling XML input from potentially untrusted sources or external APIs.
