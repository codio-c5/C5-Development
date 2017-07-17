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


**Fermat's Little Theorem** says that for any integer a, the number a p − a is an integer multiple of p. The modular arithmetic formula shows this as:

```a^p ≡ a ( mod o )```


If a is not a multiple of p, this mathematical truth becomes:

```a^(p − 1) ≡ 1 ( mod p )```

In English, this means that if you multiply a by itself p-minus-1 and then subtract 1, the result is divisable by p as long as p is a prime number and a is an integer that is not divisible by p. (me: review my p's and a's) It also means that the left side of the equation will always be equal to 1 for a modulus of P and the given conditions.

This is important for cryptography because it hints at a possible mathematical identity. Recall that in everyday arithmetic, a multiplicative identity is when a multiplication always results in the number 1 being the answer. Fermat's Little Theorem says proves that you get a modular identity if you choose certain numbers. This mathematical truth, as you will see, became the basis for public key cryptography.

>Every prime number [p] divides necessarily one of the powers –1 of any [geometric] progression [a, a2, a3, ...] [that is there exists t such that p divides at – 1], and the exponent of this power [t] divides the given prime –1 [divides p – 1]; and, after one has found the first power [t] that satisfies the question, all those whose exponents are multiple of the exponent of the first one satisfy similarly the question [that is, all multiples of the first t have the same property].


[Recall that 2 numbers are congruent if they only share one common divisor of 1.]

Huh? That's Fermat's Little Theorem. He discovered the mathematical relationship in 1640. In 1783, Leonhard Euler ("Oiler") expanded that theorem as Euler's Totient function.

## Paul to describe what the heck this is and why it's relevant....
Will do. It's the basis for the Internet as we know it. It should be moved back before the 2.8x RSA stuff but after the modular arithmetic that I'm writing: 2.X1 Modular Arithmetic, 2.X2 Fermat, 2.X3 RSA slides.

