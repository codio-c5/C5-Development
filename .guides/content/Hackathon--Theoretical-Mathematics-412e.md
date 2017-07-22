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

**Fermat's Little Theorem** says that for any integer A and prime number P, if you raise A to the power of P, then the result is congruent (i.e., equivalent) to multiplying A by itself P times. The modular arithmetic formula shows this as:

```A^P ≡ A ( mod P )```
$A^P ≡ A (mod P$)

Fermat also discovered that if P is a prime number and A is not a multiple of P, this formula becomes:

```A^(P − 1) ≡ 1 ( mod P )```

$A^P-1 ≡ 1 (mod P$)

In English, this means that if you multiply A by itself P minus 1 times, the result is divisable by P. It also means that the left side of the equation will always be equal to 1 for a modulus of P.

This relationship is important in cryptography because it hints at a possible mathematical inverse relationship. Recall that in everyday arithmetic, if you multiply a number by its reciprical the answer is always 1. For instance, the reciprical of 4 is 1/4 or .25 and if you multiply 4 by .25 you get 1. 

Fermat's Little Theorem gives a modular inverse if you choose certain numbers.

Fermat discovered this mathematical relationship in 1640. More than one hundred years later, Leonhard Euler ("Oiler") proved Fermat's Little Theorem and expanded it to what is now know as Euler's Totient Theorem. 

    a^φ ( P ) ≡ 1 ( mod P )
    
    $a^φ ( P ) ≡ 1 ( mod P $)

It depends on additional relationships between integers and prime numbers: A and P must be coprime positive integers, which means the only common denominator they share is 1. 

This again shows an inverse mathematical relationship. Nearly two hundred years later, Rivest, Shamir and Adelman used this and other theorems to find numbers that are inverses of each other. Inverse numbers are the basis for RSA encryption where one number encrypts a message and its inverse decrypts it or vice versa.
