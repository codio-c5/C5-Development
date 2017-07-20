## Familiar Faces

### Rivest Shamir Adleman (RSA) 
In the Public Key Cryptography lesson, you learned how the RSA algorithm works, using prime numbers and modular arithmetic to create a unique value between an exchanged public keys and your private key. The RSA algorithm can be applied to the hash value, creating a digital signature. 


<br>
<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/Nibs.jpg" alt="https://commons.wikimedia.org/wiki/File% A forest of for sale signs in Oughtibridge UK.By Infrogmation of New Orleans [CC BY 2.0], via Wikimedia Commons">
  <figcaption style="font-size: 0.8em; text-align: left;">Fountain pen nibs.
  </br>
By Francis Flinch (Own work) [CC BY-SA 4.0], via Wikimedia Commons</figcaption>
</figure>

### Digital Signature Algorithm (DSA) 
In 1991 NIST proposed DSA for use and adopted it in their Digital Signature Standard (DSS) 1994. In DSA, signing a message starts with creating one value, S~1~, and using it to sign the message's hash value, which creates a second value S~2~. Together, the values S~1~S~2~ are the digital signature, and are sent with the message. The recipient can calculate its inverse to verify the signature.

DSA is as fast as RSA in creating signatures, but is 10-40 times slower that RSA in signature verification.



### Elliptic Curve Digital Signature Algorithm(ECDSA)
A variant of DSA, the ECDSA calculates S~1~S~2~ using inverse points on an elliptic curve, as described in ECC earlier.  

As with ECC, the advantage of ECDSA is size. While signature sizes are the same for ECDA and DSA, an ECDSA public key is much smaller than its DSA equivalent.