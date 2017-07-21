### Note the math involved in this algorithm. You can see how much more mathematically complicated this algorithm is compared to the symmetric key algorithms DES and AES in Unit 1.

It's based on modular arithmetic and prime numbers.
Key generation by Bob:

Select $p$ and $ q$. they are both prime numbers where $p\neq q$

Calculate $n=p\times q$.

Calculate $φ(n)=(p-1)(q-1)$

This is **Euler’s phi function**

Select $e$ where $1 < e < φ(n)$, $gcd⁡(e,φ(n))=1$

Calculate $d$.  $d=e^{-1}\bmodφ(n)$

This yields a public key: $(e,n)$  and a private key: $(d,n)$.

Encryption by Alice (of a message for Bob)

Plaintext: (message) $m < n$

Ciphertext: $C=M^e \bmod n$

Decryption by Bob (of the message from Alice)

Ciphertext: $c$

Plaintext: $m= C^d \bmod n$

{Submit Answer!|assessment}(free-text-2750669850)

|||guidance
**Instructor's Note:** Asymmetric key algorithms become increasingly complex as computing power evolves. The more complex the algorithm, more time and computing power is required by those seeking to crack the code. |||