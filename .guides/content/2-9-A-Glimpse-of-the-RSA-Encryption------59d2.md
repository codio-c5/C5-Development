

Taught as a Hackathon? Leave it out?

•Key generation by Bob:

•Select p,q  p and q both prime, p≠q

•Calculate    n=pxq

•Calculate φ(n)=(p-1)(q-1)   (Euler’s phi function)

•Select e              1<e <φ(n),〖 gcd〗⁡(e,φ(n))=1

•Calculate d        d= e^(-1) mod φ(n)

•Public key  (e,n)              Private key (d,n)

•Encryption by Alice (of a message for Bob)

•Plaintext (message)    M<n

•Ciphertext                   C= M^e  mod n

•Decryption by Bob (of the message from Alice)

•Ciphertext                    C

•Plaintext                   M= C^d  mod n

