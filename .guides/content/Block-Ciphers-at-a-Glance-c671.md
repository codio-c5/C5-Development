With the advent of powerful computers, modern cryptography has moved away from substitution ciphers and on to block ciphers.  In **block encryption,**  rather than working on a stream of data one bit at a time, it works on a block of data. In a block cipher, plaintext is broken into units of a specific length, and combined with a key of a specific length. The length of the key determines the strength of the cipher.  While longer keys are more secure, they are also less efficient, so you need to find the right balance. 

**Data Encryption Standard (DES)** is one example of a block cipher. In DES, one block consists of 64 bits. DES uses a key of 56 bits, and given increased computing power, it is no longer considered secure. DES encrypts 64 bits at a time. 

||| guidance
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

 In 1998, NIST held a competition to replace DES with an encryption standard that would be more secure, yet still efficient.  In 2000, the winner was the Rijndael algorithm created by Vincent Rijmen and Joan Daemen of Belgium. It became known as the **Advanced Encryption Standard (AES)** Today, AES is used extensively worldwide, and is gradually replacing DES and 3DES. AES uses 128 bits in a process that combines substitution  with permutation that is referred to as a **substitution-permutation network** in cryptography.  


||| guidance
**Instructor's Note:** You can use this schematic of the AES encryption algorithm to show that it is rather more rigorous in its approach. 

<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/aes.jpg" alt="Source: Figure 5.1 AES Encryption Process” <u>Cryptography and Network Security: Principles and Practice.</u> Stallings, W. ©2013 Pearson. Reprinted with permission from author.d">
  <figcaption style="font-size: 0.8em; text-align: left;"> The AES Encryption Process.
  </br>
  Source: "Figure 5.1 AES Encryption Process” <u>Cryptography and Network Security: Principles and Practice.</u> Stallings, W. ©2013 Pearson. Reprinted with permission from author.</figcaption>
</figure>

|||