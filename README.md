# PolyChecker

Used search website and identify the use of cdn[.]polyfill[.]io

When using this CDN, you may be redirecting users to some maliicous websites.

Fix: Replace all instances of cdn[.]polyfill[.]io with polyfill-fastly.io (Known good snapshot) or utilize a locally hosted version.

Ref:  https://polykill.io/

Usage: Provide the tool a domain or subdomain and it will parse the html to look for cdn[.]polyfill[.]io. 

(Coming soone)If multiple domains or subdomains are of interest, you can use the -f option and it will utilize a file filled with domains/subdomains instead of a single domain. When using -f, ensure that there is one domain per line:

Ex:

1> hello.world

2> world.hello.world

3> big.hello.world/europe

4> https://hello.world

5> http://hello.word/eu
