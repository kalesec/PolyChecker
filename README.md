# PolyChecker

Used to search website html and identify the use of cdn[.]polyfill[.]io

When using this CDN, you may be redirecting users to maliicous websites.

Fix: Replace all instances of cdn[.]polyfill[.]io with polyfill-fastly.io (Known good snapshot) or utilize a locally hosted version.

Ref:  https://polykill.io/

Usage: Provide the tool a domain or URL and it will parse the html to look for cdn[.]polyfill[.]io. 