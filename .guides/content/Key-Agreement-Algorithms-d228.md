### Whitfield Diffie and Martin Hellman thought of another approach that takes advantage of both public key and symmetric cryptography called key agreement. It allows two users to securely agree on a shared key via a public key exchange.  

Once they agree upon a shared key, it can be used like a symmetric key for secure message exchange. This process is also known as the **Diffie-Hellman key exchange.**  Independently, Ralph Merkle arrived at a similar approach around the same time.


<figure class="snippetimg" style="margin: 0 auto;width:50%">
  <img src=".guides/img/keyagmt.jpg" alt="Medieval key pair. By: The Portable Antiquities Scheme/ The Trustees of the British Museum [CC BY-SA 2.0], via Wikimedia Commons.>
<figcaption style="font-size: 0.6em; text-align: left;">A medieval key pair.    
  </br>
<figcaption style="font-size: 0.8em; text-align: left;">From The Portable Antiquities Scheme/The Trustees of the British Museum [CC BY-SA 2.0], via Wikimedia Commons</figcaption>
</figure>


**Elliptic Curve Diffie-Hellman Key Agreement** is another example of a key agreement algorithm.  As with ECC, points on an elliptic curve are used to generate the session key. It has been included in the cipher suite for key agreement/exchange in TLS/SSL and Bluetooth (LE) protocols, due to its relatively small key size.


 