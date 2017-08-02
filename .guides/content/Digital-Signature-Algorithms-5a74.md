## Three Examples of Digital Signature Algorithms

### Rivest Shamir Adleman (RSA) 
In the "Public Key Cryptography" lesson earlier, you learned how the RSA algorithm works. It uses prime numbers and modular arithmetic to create a unique value between a public key and your private key. The RSA algorithm can be applied to the hash value, creating a digital signature. 


<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/Nibs.jpg" alt="https://commons.wikimedia.org/wiki/File% Fountain pen nibs.By Francis Flinch (Own work) [CC BY-SA 4.0], via Wikimedia Commons.">
  <figcaption style="font-size: 0.8em; text-align: left;">Fountain pen nibs.
<br>
By Francis Flinch (Own work) [CC BY-SA 4.0], via Wikimedia Commons.</figcaption>
</figure>

### Digital Signature Algorithm (DSA) 
In 1991, NIST proposed DSA for use and adopted it in their Digital Signature Standard (DSS) in 1994. In DSA, signing a message starts with creating one value, **S~1~,** and using it to sign the message's hash value, which creates a second value, **S~2~.** Together, the values **S~1~S~2~** are the digital signature, which is sent with the message. The recipient can calculate its inverse to verify the signature.

DSA is as fast as RSA in creating signatures, but it is 10-40 times slower than RSA in signature verification.


### Elliptic Curve Digital Signature Algorithm (ECDSA)
A variant of DSA, the ECDSA calculates **S~1~S~2~** by using inverse points on an elliptic curve, as described in "Elliptic Curve Cryptography (ECC)" in the "Public Key Cryptography" lesson.  

As with ECC, the advantage of ECDSA is size. While signature sizes are the same for ECDA and DSA, an ECDSA public key is much smaller than its DSA equivalent. This is useful for small devices with limited processors.