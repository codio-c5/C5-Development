## Fermat's Little Theorem 
<br>
<figure class="snippetimg" style="margin: 10 auto;width:50%">
  <img src=".guides/img/Fermat.jpg" alt="Lawyer and mathematician Pierre de Fermat (1601 – 1665) 
*Source: Wikimedia Commons*">
  <figcaption style="font-size: 0.8em; text-align: left;">Lawyer and mathematician Pierre de Fermat (1601–1665). 
</brS>Source: Wikimedia Commons.</figcaption>
</figure>

Fermat ("Fair-mah") is credited with creating modern number theory. His interest in pure mathematics also helped create the basis for calculus and eventually to public key encryption.

[Learn more about Fermat.](http://www.storyofmathematics.com/17th_fermat.html.)

**Fermat's Little Theorem** says that for any integer $A$ and prime number $N$, if you raise $A$ to the power of $N$, then the result is congruent (i.e., equivalent) to multiplying $A$ by itself $N$ times. The modular arithmetic formula shows this as:

$A^N \equiv A \bmod N$

Fermat also discovered that if $N$ is a prime number and $A$ is not a multiple of $N$, this formula becomes:

$A^{(N-1)} \equiv 1 \bmod N$

In English, this means that if you multiply $A$ by itself $N$ minus $1$ times, the result is divisible by $N$. It also means that the left side of the equation will always be equal to $1$ for a modulus of $N$.

This relationship is important in cryptography because it hints at a possible multiplicative inverse relationship. Recall that in everyday arithmetic, if you multiply a number by its reciprocal the answer is always $1$. For example, the reciprocal of $4$ is $\frac{1}{4}$ or $.25$ and if you multiply $4$ by $.25$ you get $1$. Public key cryptography uses that type of relationship to work. The general idea is to multiply plaintext by a number and get ciphertext. Multiply the ciphertext by the reciprocal of the number and you get the plaintext back.

**Euler's Totient Function** Fermat discovered this mathematical relationship in 1640. More than one hundred years later, Leonhard Euler ("Oiler") proved Fermat's Little Theorem and generalized it to what is now know as Euler's Totient Theorem. Euler's Totient function is related to that theorem and forms the basis for RSA encryption.

$A^{\phi(N)} \equiv 1 \bmod N$

Euler's Totient Theorem depends on additional relationships between integers and prime numbers: $A$ must be greater than $N$ and both must be coprime positive integers, which means the only common denominator they share is $1$. 

Euler's Totient function provides the multiplicative inverse relationship that Rivest, Shamir and Adelman used two hundred years later. They used it and other math to find numbers that are inverses of each other. Inverse numbers are the basis for RSA encryption where one number encrypts a message and its inverse decrypts it or vice versa.

[Learn more about how RSA uses Euler's Totient function.](http://web.math.princeton.edu/math_alive/1/Notes2.pdf)



