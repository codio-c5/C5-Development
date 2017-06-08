
2.15 (S19) Use of Key Agreement Protocols (Paul)

Taught as expository (perhaps building to growth hack)

•Users could create random private/public keys each time they communicate

             OR

•Users could create private and public keys and publish the public key

 

•Problem: Vulnerable to Man-in-the-Middle-Attack

 

Comments: Now consider a simple protocol that makes use of the Diffie-Hellman calculation. Suppose that user A wishes to set up a connection with user B and use a secret key to encrypt messages on that connection. User A can generate a one-time private key XA, calculate YA, and send that to user B. User B responds by generating a private value XB, calculating YB, and sending YB to user A. Both users can now calculate the key. The necessary public values q and a would need to be known ahead of time. Alternatively, user A could pick values for q and a and include those in the first message. 

 

