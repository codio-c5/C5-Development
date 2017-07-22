

### In 1977, three researchers at the MIT Laboratory of Computer Science came up with the RSA Encryption algorithm. Inspired by the work of Diffie and Helman, RSA (Named after inventors Rivest, Shamir, and Adleman) was the first viable and publically available public key encryption algorithm and became the foundation for secure global communication on the Internet.

<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/RivestShamirAdleman.PNG"  alt="Ronald Rivest, Adi Shamir, and Leonard Adleman, Creators of RSA Encryption. . *Source: From left to right: by Ronald L. Rivest (Own work) CC BY-SA 4.0; by Erik Tews (Own work) CC BY-SA 3.0; by Len Adleman, (Own work) CC BY- SA 3.0, via Wikimedia Commons.*
">
  <figcaption style="font-size: 0.8em; text-align: left;">Ronald Rivest, Adi Shamir, and Leonard Adleman, Creators of RSA Encryption. 
<br>
Source: From left to right: by Ronald L. Rivest (Own work) CC BY-SA 4.0; by Erik Tews (Own work) CC BY-SA 3.0; by Len Adleman, (Own work) CC BY- SA 3.0, via Wikimedia Commons.</figcaption>
</figure>

Rivest, Shamir, and Adelman discovered that they could create two numbers that are the inverse of each other. They used mathematics discovered centuries earlier to do for this purpose [[psery: we need to tie this into the modular arithmetic and fermat's/euler's sections]]. This relationship satisfies the fundamental requirement of public key encryption: one number is used as a public key and its inverse as the private key or vice versa. In other words, enter plaintext into the RSA algorithm using one number to get ciphertext; plug the ciphertext into the same formula using the other number and you get the plaintext back again.

RSA's security depends on the difficulty of factoring large numbers. Factoring a number means finding two numbers that when multiplied together produce the original number. RSA starts by multiplying two prime numbers to create a modulus and then deriving the public and private keys from that seed. Finding the right prime numbers is the difficult part but the centuries old math provided the right ingredients. However, without knowing the prime numbers, and if they're large enough even today's fastest computers can not factor them.  The larger the prime numbers used, the more difficult it becomes, and the more secure the encryption. 

Another advantage of RSA is that it can be used to sign a message to verify authenticity, which you'll learn more about in the next unit.

A disadvantage of RSA is that it requires more processing power and memory than other similar methods.

RSA is included in the cipher suite for key agreement/exchange in TLS/SSL (Transport Layer Security/Secure Socket Layer). 

The Internet as we know it exists because RSA made e-commerce possible. RSA brilliantly combines mathematics spanning centuries and, in the case of the Euclidean algorithm, millenia.

|||guidance 
**Instructor's note:**  The optional Hackathons at the end of the lesson are best integrated after this page.  If you plan to use them, they fit here nicely.
|||



