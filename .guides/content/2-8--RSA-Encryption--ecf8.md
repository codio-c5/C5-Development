[add introduction to modular arithmetic in previous section]

![.guides/img/RivestShamirAdleman](.guides/img/RivestShamirAdleman.PNG)
 Ronald Rivest, Adi Shamir, and Leonard Adleman, Creators of RSA Encryption.
 
*Source: From left to right: by Ronald L. Rivest (Own work) CC BY-SA 4.0; by Erik Tews (Own work) CC BY-SA 3.0; by Len Adleman, (Own work) CC BY- SA 3.0, via Wikimedia Commons.*
 
In 1977, three researchers at the MIT Laboratory of Computer Science came up with the RSA Encryption algorithm. RSA was the first viable and publically available public key encryption algorithm [1] and  became the foundation for secure global communication unhindered by the necessity of explicit key distribution...

The Internet as we know it exists because RSA made e-commerce possible. RSA encryption allows two strangers to securely and confidently communicate with each other.

[author's note]
Without a profit motive, the Internet would still be the sleepy domain of nerds, universities and the military that it was until the early-to-mid 1990's. The Internet exploded in uses and users when business figured out how to use the Internet to make money over the Internet, investment flowed in to build up the underlying infrastructure - faster fibre, data centers, software, devices, etc. Constant investment and innovation has let to the ubiquity and omniprecense of the Web [this is !=PC but oh well...]

And securing Internet communications is possible because modulus m of a-to-the-power-of-m-minus-1 is congruent to 1. In other words, A to the power of (P − 1) − 1 is divisible by P, when P is a prime number and A is an integer that is not divisible by P; alternatively this mathematical truth can be expressed in modular arithmetic as a^(m-1) ≡ 1(mod m).

[Recall that 2 numbers are congruent if they only share one common divisor of 1.]

Huh? That's Fermat's ("Fair-ma") Little Theorem. He discovered the mathemtical relationship in 1640. In 1783, Leonhard Euler ("Oiler") expanded that theorem as Euler's Totient function. 

Nearly 200 years later Rivest, Shamir and Adelman discovered that by combining Fermat's Little Theorem, Euler's Totient Function (a generalization of Fermat's Little Theorem), along with aid of other mathematical wonders like the Chiness Remainder Theorem, the Euclidean Algorithm, they could calculate two numbers that are the inverse of each other. This relationship satisfies the fundamental requirement of Public Key encryption: one number can be used as a public key and its inverse as the private key.

RSA brilliantly combines mathematics spanning centuries and, in the case of the Euclidean Algorithm, millenia.

•Included in the cipher suite for key agreement/exchange in TLS/SSL (Transport Layer Security/Secure Socket Layer)



