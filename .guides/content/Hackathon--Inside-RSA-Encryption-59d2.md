### Note the math involved in this algorithm. You can see how much more mathematically complicated this algorithm is compared to the DES and AES symmetric key algorithms in Unit 1.

It's based on modular arithmetic and prime numbers.

Key generation by Bob:

Select $p$ and $q$. they are both prime numbers where $p\neq q$

Calculate $n=p\times q$.

Calculate the **Euler's Totient funtion** (also referred to as just **Phi**):

$$\phi(n)=(p-1)(q-1)$$

Choose an integer $e$ where $1 < e < \phi(n)$ and $e$ and $\phi(n)$ are coprime $gcd⁡(e,\phi(n))=1$ ($e$ and $\phi(n)$ do not share any divisors other than 1).

Calculate d so that $\frac{d}{b}\times e$ is congruent with $1 \bmod \phi(n)$ or $d*e \equiv 1 \bmod \phi(n)$ 

This yields a public key: $(e,n)$  and a private key: $(d,n)$.

Encryption by Bob (of a message for Alice). If, for instance, Bob wants to send the message "Meet me at the ...", he would first obtain Alice's public key $(e,n)$, convert the text into integers, and pad the beginning and end with random numbers to prevent cryptanalysis. The message, which has been converted into a number, must be smaller than the modulus $n$.

Plaintext: message $m$, where $m < n$

Bob would then encrypt the plaintext into ciphertext as follows:

Ciphertext: $c=m^e \bmod n$

Decryption by Alice (of the message from Bob $c$) using Alice's private key $(d,n)$

Ciphertext: $c$

Plaintext: $m= c^d \bmod n$

{Submit Answer!|assessment}(free-text-2750669850)

|||guidance
**Instructor's Note:** Asymmetric key algorithms become increasingly complex as computing power evolves. The more computationally complex the algorithm and often the keysize, more time and computing power is required by those seeking to crack the code. 
|||
