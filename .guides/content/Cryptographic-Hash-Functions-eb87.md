## The Secure Hash Algorithm (SHA)

### In 1993, the NSA produced the first Secure Hash Algorithm, now referred to as SHA-0.  

### In 1995, the NSA released an improved version, SHA-1, which was published by NIST as the federal information processing standard.Like SHA-0, SHA-1 produces a 160 bit hash value.  SHA-1 was used widely for TLS and SSL, PGP, SSH, S/MIME, and IPSec.
 

Recently, cryptanalysts from the CWI Institute and Google were able to generate a collision using two different files that have the same hash. As early as 2005, theoretical attacks developed for SHA-1 suggested the algorithm may not be secure enough for ongoing use.   SHA-1 was deprecated in 2011 and disallowed for use in digital signatures in 2013. Common browsers such as Chrome and Internet Explorer no longer support SSL certificates that use SHA-1.

Google revealed a SHA-1 vulnerability in early 2017 and the software repository system Subversion quickly became a victim:
https://www.bleepingcomputer.com/news/security/sha1-collision-attack-makes-its-first-victim-subversion-repositories/

**In the news:**  
[Learn more about the breaking of SHA-1](http://hackaday.com/2017/02/23/shattered-sha-1-is-broken/)



