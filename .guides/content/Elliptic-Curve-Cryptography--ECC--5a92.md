### In 1985, Neal Koblitz and Victor S. Miller independently discovered that the mathematical formula for elliptic curves could yield a public and private key pair. 
<br>
<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/ellipticalcurves.PNG"  alt="Elliptical curves.  *By Oscarpettersson (Own work) [CC BY-SA 3.0, via Wikimedia Commons.*
">
  <figcaption style="font-size: 0.8em; text-align: left;">Elliptical curves. 
</br>
By Oscarpettersson (Own work) [CC BY-SA 3.0, via Wikimedia Commons.</figcaption>
</figure>

The process involves choosing two points on the curve, and using them to calculate a third point. As with the prime numbers used in RSA, it is easy to calculate a third point when you have the two original points, but exceptionally difficult to find the original points from the third.

## Size Matters 
The advantage of elliptic curve cryptography over RSA is that the key size is much smaller, but the level of security is greater.For example, a 256 bit ECC key is as secure as an RSA 3072 bit key.

This is important for mobile devices, which often have small processors and storage capacity. It is included in Bluetooth Low Energy (LE) protocols.

It is also included in the cipher suite for key agreement exchange in [ the cipher suite TLS/SSL protocols.](https://en.wikipedia.org/wiki/Cipher_suite)
||| guidance

**Instructor's Note:**
The links below offer more information about the ECC inventors.
[Learn more about Neal Koblitz]( http://www.washington.edu/news/2007/11/08/neal-koblitz-deciphering-the-cryptographer/)
 [Learn more about Victor S. Miller](https://www.youtube.com/watch?v=I-248cGfwy4)