

## Cryptography and Modular Arithmetic

### Today, cryptography methods continue to evolve as cryptanalysis techniques emerge and computing power grows.  In asymmetric cryptography, mathematics and the way numbers work provides new encryption methods that are increasingly secure.

||| definition
In **modular arithmetic**  calculations are performed by dividing by the size of a circle, called the **modulus,** or mod for short. The resulting remainder is the answer. 
|||

Do you remember created a **number line** back in grade school?

```
<   0   1   2   3   4   5   6   7   8   9   10   11   12  13... >
```
Number lines are useful for visualizing mathematical operations like addition and subtraction. For instance,  by moving from 0 to 1 and then from 1 to 2 and you have calculated ```1 + 1```. You can also multiply two numbers, for instance ```2 x 3``` by first moving from 0 to 2, then from 2 to 4 and once again from 4 to 6 to get the answer 6.

Modular arithmetic starts with imagining a number line as a circle. The circle can vary in size.  Let's start with a familiar circle with a modulus, or size, of 12.   

<br>
<figure class="snippetimg" style="margin: 0 auto;width:50%">
  <img src=".guides/img/Clockface.PNG" alt="Antique skeleton keys. Sourced under CC 0 public domain. publicdomainpictures.net">
  <figcaption style="font-size: 0.8em; text-align: left;">
  <br> A circular number line.   
  </br>
By AxG, via Wikimedia Commons.  </figcaption>
</figure>

To add two numbers like 9 and 4, start at the top and go 9 increments clockwise to 9. Now go 4 increments from 9 and you end up at 1. This example is immediately recognizable as a clock but is also an example of **modular arithmetic.** In fact, Modular arithmetic is often referred to as *clock arithmetic.* 

Compare this with the horizontal number line.  There, adding 9 and 4, you end up at 13. Using the circular number line you end up at 1.


Here's a little more on the math. The example adds two numbers, 9 and 4, and then divides by 12. Twelve can go into 13 once and leaves a remainder of 1. When using everyday arithmetic, we'd continue the process by dividing the remainder 1 by 12 and end up with a fractional result of 1/12 or 1.0833. However, when using modular arithmetic the result ***is*** the remainder. Stated in modular arithmetic terms the answer is 13 mod 12 equals 1, or alternatively 13 (mod 12) equals 1. The result is stated as 1 is congruant with 13 mod 12.

Modular arithmetic describes the size of the circle as the modulus. The above modulus is 12, ```mod = 12```. Instead of using the concept of something equal (=) to something, you use the concept of congruence, designated with the Congruant symbol (≡).

```x ≡ y (mod n)```


<<<<<<< HEAD:.guides/content/Alternate-2-8A-for-Paul-to-consider--Across-the-Disciplines--Mathematics--paul-yes--this-works-for-me--abbc.md
(Some authors use = instead of ≡; in this case, if the parentheses are omitted, this generally means that "mod" denotes the modulo operation, that is, that 0 ≤ a < n).
=======
This means that x is congruent with y for a given modulus of n. So if y = 1 and n = 12, then y will be 13. Actually, x can be 13, 26, 39, or any integer that's a multiple of 13.

## Check Your Knowledge
{Check It!|assessment}(multiple-choice-146398319)
{Check It!|assessment}(multiple-choice-3027256850)
{Check It!|assessment}(multiple-choice-259300797)

>>>>>>> 25458799fde6019c33dd51dc35bf076c7eb2716c:.guides/content/Across-the-Disciplines--Mathematics--abbc.md

Along with prime numbers, modular arithmetic is important in cryptography because it enables two parties to encrypt and decrypt messages using an indecipherable key pair that no one else can calculate. It is essential to RSA encryption.

