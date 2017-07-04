||| Number Theory

Number Theory is the study of the properties of numbers and how they relate to each other. For instance, we're all familiar with odd - 2, 4, 6, ... - and even numbers - 1, 3, 5,... https://nrich.maths.org/4352 

Arithmetic is part of Number Theory. Elementary arithmetic operations such as addition and multiplication are familiar to all of us. So should properties like the following ones.

Commutative property, where the order that two numbers are multiplied do not affect the result:
  x * y = y * x
  2 * 3 = 3 * 2 = 6

Associative property, that says the grouping of multiplication or addition can be re-ordered without affecting the result:
  ( x * y) * z = x * (y * z)
  (2 * 3) * 4 = 2 * (3 * 4) = 24

Distributive property, ensures that multiplication takes precedence over addition.
  x * (y + z) = x * y + x * z
  2 * (3 + 4) = 2 * 3 + 2 * 4 = 14

Identity element, which is a property that you'll see is very important with respect to public key encryption.
  x * 1 = x
  2 * 1 = 2
  3 * 1 = 3

Prime numbers are important part of number theory. A prime number is an integer that is only divisible by 1 and itself. For instance, 43 is prime because it can be divided by 1 or 43 but nothing else. Prime numbers are useful in many areas of mathematics, and especially so in cryptography.

||| Modular Arithmetic

If you draw a line using a ruler and mark each inch or centimeter as 0, 1, 2, etcetera you have created a number line. 

<--0--1--2--3--4--5--6--7--8--9--10--11--12--13--...-->

Number lines are useful for visualizing mathematical properties and operations. You can use a them to perform simple calculations such as addition.

For instance,  by moving from 0 to 1 and then from 1 to 2 and you have calculated 1 plus 1. You can also multiply two numbers, for instance 2 x 2 by first moving from 0 to 2 and then from 2 to 4 and your get the answer 4. This is trivial, of course, but will help understand the mathematics essential to public key cryptography.

You can also create a number line as a circle. For example, envision the previous line as a string wrapped around a circle of 12 increments. Let's say you want to add two numbers 9 and 4. Imagine starting at 0 and go 9 increments to 9. Next go 4 increments from 9 and you end up at 1. This example is immediately recognizable as a clock but is also an example of Modular arithmetic. In fact, Modular arithmetic is often referred to as "clock arithmetic". It's something we do every day.

.guides/img/circular-number-line.png

If you use horizontal number line to add 9 and 4, you end up at 13. However, using the circular number line you end up at 1. Modular arithmetic performs a calculation by dividing by the "size" of a circle and returns a result as the remainder of a division. The above example adds two number (9 and 4) and then divides by 12. Twelve can go into 13 once and leaves a remainder of 1. When using everyday arithmetic, we'd continue the process by dividing the remainder 1 by 12 and end up with a fractional result of 1.0833. However, when using Modular arithmetic the result _is_ the remainder.

This example, stated in Modular arithmetic terms is 13 mod 12, or alternatively 13 (mod 12). 
the modulus is only the remainder of .




Modular arithmetic describes the size of the circle as the modulus. The above modulus is 12, (mod = 12). Instead of using the concept of something equal (=) to something, we use the concept of congruence, designated with the symbol (≡).

x ≡ y (mod n)

This means that x is congruent with y for a given modulus of n. So if y = 1 and n = 12, then y will be 13. Actually, x can be 13, 26, 39, or any integer that's a multiple of 12.

"Modular arithmetic can be handled mathematically by introducing a congruence relation on the integers that is compatible with the operations on integers: addition, subtraction, and multiplication. For a positive integer n, two numbers a and b are said to be congruent modulo n, if their difference a − b is an integer multiple of n (that is, if there is an integer k such that a − b = kn). This congruence relation is typically considered when a and b are integers, and is denoted

    a ≡ b ( mod n ) . {\displaystyle a\equiv b{\pmod {n}}.} {\displaystyle a\equiv b{\pmod {n}}.}

(some authors use = instead of ≡; in this case, if the parentheses are omitted, this generally means that "mod" denotes the modulo operation, that is, that 0 ≤ a < n).

The number n is called the modulus of the congruence."

You can use modular arithmetic to perform operations similar to every day arithmetic. Here are some of the following properties that will be useful in this course.





Modular arithmetic is used in many areas of mathematics but is especially important in cryptography. 

[add introduction to modular arithmetic in previous section]

.guides/img/RivestShamirAdleman Ronald Rivest, Adi Shamir, and Leonard Adleman, Creators of RSA Encryption.

Source: From left to right: by Ronald L. Rivest (Own work) CC BY-SA 4.0; by Erik Tews (Own work) CC BY-SA 3.0; by Len Adleman, (Own work) CC BY- SA 3.0, via Wikimedia Commons.

In 1977, three researchers at the MIT Laboratory of Computer Science came up with the RSA Encryption algorithm. Inspired by the work of Diffie-Helman[verify reference ps], RSA was the first viable and publically available public key encryption algorithm [1] and became the foundation for secure global communication unhindered by the necessity of expensive symmetric key distribution systems.

The Internet as we know it exists because RSA made e-commerce possible. RSA encryption allows two strangers to securely and confidently communicate with each other.

[author's note] Without the ability of two or more strangers to securely communicate with each other, the Internet would still be the sleepy domain of nerds, universities and the military that it was until the early-to-mid 1990's. Use of the Internet exploded once it became possible to use it for commerce. Once big money was made, a tidal wave of investment flowed in and built the underlying infrastructure - faster fibre, data centers, software, devices, etc. Constant investment and innovation has let to the ubiquity and omnipresence of the Web [this is !=PC but oh well...]

Nearly 200 years later Rivest, Shamir and Adelman discovered that by combining Fermat's Little Theorem, Euler's Totient Function (a generalization of Fermat's Little Theorem), along with aid of other mathematical wonders like the Chiness Remainder Theorem, the Euclidean Algorithm, they could calculate two numbers that are the inverse of each other. Actually they're the modulo inverse of each other, but this relationship satisfies the fundamental requirement of Public Key encryption: one number can be used as a public key and its inverse as the private key.

RSA brilliantly combines mathematics spanning centuries and, in the case of the Euclidean Algorithm, millenia.

• Included in the cipher suite for key agreement/exchange in TLS/SSL (Transport Layer Security/Secure Socket Layer)
