Note the math involved in this algorithm. You can see how much more mathematically complicated this algorithm is compared to the symmetric key algorithms DES and AES in Unit 1.

It's based on Modular arithmetic and
Key generation by Bob:

    Select p,q p and q both prime, p≠q

    Calculate n=p x q

    Calculate φ(n)=(p-1)(q-1) (Euler’s phi function)

    Select e 1<e <φ(n), gcd⁡(e,φ(n))=1

    Calculate: d d= e^-1^ mod φ(n)

    Public key: (e,n) Private key: (d,n)

Encryption by Alice (of a message for Bob)

    Plaintext: (message) M<n

    Ciphertext: C= M^e^ mod n

Decryption by Bob (of the message from Alice)

    Ciphertext: C

    Plaintext: M = C^d^ mod n

{Submit Answer!|assessment}(free-text-2750669850)

|||guidance Instructor's Note: Asymmetric key algorithms have become increasingly complex as computing power evolves. The more complex the algorithm, more time and computing power is required by those seeking to crack the code. |||