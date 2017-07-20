## Fermat's Little Theorem 
<br>
<figure class="snippetimg" style="margin: 10 auto;width:50%">
  <img src=".guides/img/Fermat.jpg" alt="Lawyer and mathematician Pierre de Fermat (1601 – 1665) 
*Source: Wikimedia Commons*">
  <figcaption style="font-size: 0.8em; text-align: left;">Lawyer and mathematician Pierre de Fermat (1601–1665). 
 Source: Wikimedia Commons</figcaption>
</figure>

Fermat ("Fair-mah") is credited with creating modern number theory. His interest in pure mathematics also helped create the basis for calculus and eventually to public key encryption.

[Learn more about Fermat.](http://www.storyofmathematics.com/17th_fermat.html.)

<<<<<<< HEAD
**Fermat's Little Theorem** says that for any integer A and prime number P, if you raise A to the power of P, then the result is congruent (i.e., equivalent) to multiplying A by itself P times. The modular arithmetic formula shows this as:

```A^P ≡ A ( mod P )```

Fermat also discovered that if P is a prime number and A is not a multiple of P, this formula becomes:

```A^(P − 1) ≡ 1 ( mod P )```

In English, this means that if you multiply A by itself P minus 1 times, the result is divisable by P. It also means that the left side of the equation will always be equal to 1 for a modulus of P.

This relationship is important in cryptography because it hints at a possible mathematical inverse property. Recall that in everyday arithmetic, if you a number by its reciprical the answer is always 1. For instance, the reciprical of 4 is 1/4 or .25. If you multiply 4 by .25 you get 1. 

Fermat's Little Theorem gives a modular inverse if you choose certain numbers.

Fermat discovered this mathematical relationship in 1640. More than one hundred years later, Leonhard Euler ("Oiler") proved Fermat's Little Theorem and expanded it to what is now know as Euler's Totient Theorem. It depends on additional relationships between integers and prime numbers. The details are involved and beyond the scope of this lesson. However, Rives, Shamir and Adelman used it to create a mathematical inverse relationship that is the basis for the RSA encryption.
=======
**Fermat's Little Theorem** says that for any integer $a$, the number $a (p − a)$ is an integer multiple of $p$. The modular arithmetic formula shows this as:

$a^p ≡ a ( mod o )$


If a is not a multiple of $p$, this mathematical truth becomes:

$a(p − 1) ≡ 1 ( mod p )$

In English, this means that if you multiply $a$ by itself p-minus-1 and then subtract 1, the result is divisable by $p$ as long as p is a prime number and a is an integer that is not divisible by $p$. ==(me: review my p's and a's)== It also means that the left side of the equation will always be equal to 1 for a modulus of $p$ and the given conditions.

This is important for cryptography because it hints at a possible mathematical identity. In everyday arithmetic a multiplicative identity is when a multiplication always results in the number 1 being the answer. Fermat's Little Theorem  proves that you get a modular identity if you choose certain numbers. This mathematical truth became the basis for public key cryptography.

Here's **Fermat's Little Theorem.** He discovered the mathematical relationship in 1640 centuries before public key cryptography.

>Every prime number $p$ divides necessarily one of the powers $–1$ of any [geometric] progression [$a, a2, a3, ...$] [that is there exists $t$ such that $p$ divides at $–1$ ], and the exponent of this power $t$ divides the given prime$–1$  [divides $p – 1$]; and, after one has found the first power $t$ that satisfies the question, all those whose exponents are multiple of the exponent of the first one satisfy similarly the question [that is, all multiples of the first $t$ have the same property].

Recall that two numbers are congruent if they only share one common divisor of $1$.

Leonhard Euler ("Oiler") expanded that theorem as **Euler's totient function** or **Euler's phi function**  which is also extensively referenced in public key cryptography. Check out the next Hackathon for more on this, and 
[explore it further here.](http://mathworld.wolfram.com/TotientFunction.html)
>>>>>>> 865bd997dca18dd565738519b6854edefc1b3c56
