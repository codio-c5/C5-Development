|||definition
A **shift cipher** is a generalization of Caesar cipher in which the key can be any number you like. In a Caesar cipher, the key is specifically 3 letters to the right.


**Shift** each letter in the message `k` letters in the alphabet

Example with `k=11`

```bash
PLaintext:  meet me after the toga party
Ciphertext: XPPE XP LQEPC ESP EZRL ALCEJ
```

## Cryptanalysis of Shift Cipher
What would it take to break the shift cipher? If you know that a ciphertext is obtained using a shift cipher, how would you get the original plaintext? In the brute force approach you try out all possible keys to determine the key space and the number of keys used. 

|||info
**Note:** We assume here that the cryptanalyst knows the language that the original plaintext is in.|||


## Growth Hack 
{Submit Answer!|assessment}(free-text-3680102054)
|||guidance
**Instructor's Note:** If k=0, then the ciphertext is the same as the plaintext.
|||

For an English alphabet, there are 26 possible keys. Why?
{Submit Answer!|assessment}(free-text-1360860550)

|||guidance
**Instructor's Note:** There are 33 letters in the Russian Cyrillic alphabet, and 36 in the Armenian alphabet, so the respective answers are 33 and 36.
|||

