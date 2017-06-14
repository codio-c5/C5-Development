A shift cipher is a generalization of Caesar Cipher in which the key can be any number you like.

**Shift** each letter in the message `k` letters in the alphabet

Example with `k=11`

```bash
meet me after the toga party
XPPE XP LQEPC ESP EZRL ALCEJ
```

## Cryptanalysis of Shift Cipher
What would it take to break the shift cipher? That is, if you know that a ciphertext is obtained using a shift cipher, how would you get the original plaintext? in the brute force approach you try out all possible keys to determine the key space and the number of keys used. 

|||info
# Note
A cipher can have multiple keys, making it much more difficult to decrypt.
|||
  |||info
# Note
We assume here that the cryptanalyst knows the language that the original plaintext is in.
|||

## Growth Hack 
For an English alphabet, there are 26 keys. Why?
{Check It!|assessment}{Submit Answer!|assessment}(free-text-1360860550)

||| **Instructor's Note:** There are 33 letters in the Russian Cyrillic alphabet, and 36 in the Armenian alphabet, so the respective answers are 33 and 36.|||

