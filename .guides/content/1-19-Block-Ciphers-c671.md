With the advent of powerful computers, modern cryptography has moved away from substitution ciphers and on to block ciphers.  In **block encryption,**  rather than working on a stream of data one bit at a time, it works on a block of data. In a block cipher, plaintext is broken into units of a specific length, and combined with a key of a specific length. The length of the key determines the strength of the cipher.  While longer keys are more secure, they are also less efficient, so you need to find the right balance. 

**Data Encryption Standard (DES)** is one example of a block cipher. In DES, one block consists of 64 bits. DES uses a key of 56 bits, and given increased computing power, it is no longer considered secure. DES encrypts 64 bits at a time. 

|||guidance
**Instructor's Note:** Here's a complex graphic describing DES. You can use it to explain to students that DES is rather more rigorous in its approach than the shift and substitution algorithms we have seen so far.

<figure class="snippetimg" style="margin: 0 auto;width:50%">
  <img src=".guides/img/DES.png" alt="Source: https://en.wikipedia.org/wiki/Data_Encryption_Standard">
  <figcaption style="font-size: 0.8em; text-align: left;"> DES diagram.
  </br>
 Source: https://en.wikipedia.org/wiki/Data_Encryption_Standard</figcaption>
</figure>

Students can explore DES further here: http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
|||

**Triple DES (3DES)** evolved as a replacement for DES. In 3DES, a 56 bit key is applied three times on each data block. This has the advantage of being more secure than a single 56-bit key,yet remains more efficient than a single longer length key.

