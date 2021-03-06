Substitution ciphers use a substitution alphabet as a key, to replace plaintext characters with different characters to create ciphertext. In its simplest form, the key is the alphabet shifted by some number, in which case it operates like a shift cipher. More complex versions rearrange the alphabet in arbitrary ways to make for slightly better encryption. Individual characters can also be replaced by multiple groupings to improve encryption—but not by much. Ciphertext is decrypted by simply reversing the process.

Substitution ciphers come in the following primary forms: 

1. Simple substitution ciphers, or **monographic** ciphers, replace a single letter with another letter with a one-to-one mapping.
2. **Polygraphic** substitution ciphers replace each letter of plaintext with one of several letter combinations from the key,

Let's create a monographic substitution cipher key as an example:

```
   ABCDEFGHIJKLMNOPQRSTUVWXYZ
   WUPZDLYKAGQJXOBCRIFTMVHNES
   ```
 

As you can see, each letter maps to only one letter. A plaintext message like "Hello world" encrypts to the ciphertext `KDJJB HBIJZ` where H is substituted with K, E is substituted with D, and so on.

Also, notice that the mapping of the letters isn't achieved simply by a consistent shifting of letters. The shift from Y to E is nothing like the shift from Z to S. (If a consistent shift were used instead, we'd be looking at a shift cipher!)


||| info
**Note:**
Substitution keys can be constructed from symbols instead of alphabetic characters. Ciphertext consisting of symbols might appear to provide more security at first glance, but a cryptologist, upon recognizing the trick, will quickly convert the symbols into characters and solve the puzzle.
|||