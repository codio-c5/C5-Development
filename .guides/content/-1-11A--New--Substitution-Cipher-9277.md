Substitution ciphers use a substitution alphabet, as a key, to replace plaintext characters with different characters to create ciphertext. In its simplest form the key is the alphabet shifted by some number, in which case it operates like a Caesar cipher. More complex versions rearrange the alphabet in arbitrary ways to make for slightly better encryption. Individual characters can also be replaced by multiple groupings to improve encryption - but not by much. Ciphertext is decrypted by simply reversing the process.

Substituion ciphers come in the following primary forms: 

1. Simple substitution, or monoalphabetic, that replace a single letter with another with a one-to-one mapping
2. Polygraphic substitution that replace each letter in the plaintext with one of several letter combinations from the key

Substitution ciphers provide little practical value in today's world so we'll only discuss the monoalphabetic version here in order to provide background. 

Let's create a simple substitution alphabet as an example:

Plaintext:                            ABCDEFGHIJKLMNOPQRSTUVWXYZ
Ciphertext (substitution alphabet):   WUPZDLYKAGQJXOBCRIFTMVHNES

A plaintext message like "Hello world" will map into the ciphertext "KDJJB HBIJZ", where H->K, e->D, etc.

Substitution ciphers can provide a little more security than shift ciphers by using a more complex substituion alphabet. However, both  suffer from a general lack of complexity. Each system creates ciphertext that is painfully similar to the plaintext. As with shift ciphers, simple substitution ciphertext retains the same word length and separation as the plaintext as do shift ciphers. Polygraphic ciphers change word length but a trained eye can quickly decode even using pen and paper. 

|||
Substitution keys can be constructed from symbols instead of alphabetic characters. Ciphertext consiting of symbols might appear to provide more security at first glance, but a cryptologist, upon recognizing the trick, will quickly convert the symbols into characters and solve the puzzle.
|||

But their biggest shortcoming is due to lack of key size and the linear relationship between encryption and decryption. The key is limited by the very small size of the alphabet or whatever symbols are used. Worse, the same mathematical formula that is used to encrypt is also used to decrypt. This means that there is no cost penalty when trying to decrypt a message compared to what is spent encrypting it. Encryption ciphers should be very, very one-sided, meaning that the cost of surrupticiously decrypting a message should be much, much, much more expensive than the cost of encrypting. That requirement is what drives all of today's encryption methods.
