|||definition
A **shift cipher** is a category of cipher in which the key can be any number you like. The Caesar cipher, in which the key is always three letters to the right, is a specific example of a shift cipher.
|||


**Shift** each letter in the message `k` letters in the alphabet

Example with `k=11`

```bash
Plaintext:  meet me after the toga party
Ciphertext: XPPE XP LQEPC ESP EZRL ALCEJ
```

## Cryptanalysis of a Shift Cipher
What would it take to break a shift cipher? If you knew that a ciphertext was created using a shift cipher, how would you get to the original plaintext? With the brute-force approach, you would try out all possible keys until you found something that worked.  

||| info

**Note:** We assume here that the cryptanalyst knows the language that the original plaintext is in. If the plaintext were in a language not understood by the cryptanalyst, discovering the key would be much more difficult because she might not recognize the words revealed by the correct key. 

|||


## Growth Hack 
{Submit Answer!|assessment}(free-text-3680102054)

||| guidance

**Instructor's Note:** If k=0, then the ciphertext is the same as the plaintext.

|||

{Submit Answer!|assessment}(free-text-1360860550)

||| guidance

**Instructor's Note:** There are 33 letters in the Russian Cyrillic alphabet, and 36 in the Armenian alphabet, so the respective answers are 32 and 35.

|||
