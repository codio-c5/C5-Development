Substitution ciphers use a substitution alphabet as a key, to replace plaintext characters with different characters to create ciphertext. In its simplest form the key is the alphabet shifted by some number, in which case it operates like a Caesar cipher. More complex versions rearrange the alphabet in arbitrary ways to make for slightly better encryption. Individual characters can also be replaced by multiple groupings to improve encryption - but not by much. Ciphertext is decrypted by simply reversing the process.

Substituion ciphers come in the following primary forms: 

1. Simple substitution ciphers, or monoalphabetic ciphers, replace a single letter with another with a one-to-one mapping
2. Polygraphic substitution ciphers that replace each letter in the plaintext with one of several letter combinations from the key

<<<<<<< HEAD
Substitution ciphers provide little practical value in today's world so we'll only discuss the monoalphabetic version here in order to provide background.
=======
Substitution ciphers provide little practical value in today's world so we'll only discuss the monoalphabetic version here in order to provide background. 

Let's create a simple substitution alphabet key as an example.
```
   ABCDEFGHIJKLMNOPQRSTUVWXYZ
   WUPZDLYKAGQJXOBCRIFTMVHNES
   ```
 

A plaintext message like "Hello world" encrypts to the ciphertext `KDJJB HBIJZ`, where H->K, e->D, etc.
>>>>>>> 70e104608c49ed70236d22998160554c5fd660b6

|||
Substitution keys can be constructed from symbols instead of alphabetic characters. Ciphertext consiting of symbols might appear to provide more security at first glance, but a cryptologist, upon recognizing the trick, will quickly convert the symbols into characters and solve the puzzle.
|||