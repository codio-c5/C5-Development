So, how do you crack a code?

Cryptanalysts first need to know what information they have to create a decoding strategy.  The elements of a code are the original plaintext, the resulting ciphertext, and the encryption/decryption key. To crack a code, your strategy depends on what you have. 

Following Kerckhoffs’s Principle, let's assume that the details of the algorithm used for encryption is known. If you know the key, then you can simply convert plaintext or ciphertext with ease.

If you don't know the key, then you have to solve for it.  If you have only ciphertext, then you use 

## Add info here
For simple ciphers, like Caesar cipher, then you can use a process called Brute Force to find the key. The process is simple: you test each possible key until you find the plaintext. 

Start with key=1 and shift the first "word", or grouping of letters, of ciphertext by that amount and look at the result. If the result is recognizable, then you may have found the key. In that case, you would decrypt the second ciphertext word and if it too is recognizable then you likely have the key. If not, then try key=2 and so on. There are only 25 possible keys so the process can be completed quickly even without a computer.

|||guidance
**Instructor's note:**  When the Ceasar cipher shifts past the end of the alphabet, it cycles back to the beginning and onto the letter specified by the key. You can also think of the alphabet as a circle where each letter has a numeric position and there is no beginning nor end. When you use that concept you enter into the world of modular arithmetic. In Modular Arithmetic the alphabet has a Modulus of 26.
https://en.wikipedia.org/wiki/Modular_arithmetic
That shift ciphers like Ceasar use modular arithetic is probably interesting only to those with a mathematical background. However, modular arithmetic is the basis for ciphers like RSA.
|||

If you have knowntext - both the plaintext and ciphertext - then the cryptanalysis process is easier. You would follow the above algorithm until you quickly discover the key. There's no guessing because the decrypted ciphertext will either match the plaintext or not.

You can also discover a key by searching in the opposite direction. You can take plaintext and apply a given key and see if the result matches the ciphertext. This process is the basis for cracking passwords.

You can still find the key if you only have part of the plaintext. For example, you might ciphertext "XPPE XP LQEPC ESP EZRL ALCEJ" but only the plaintext "party". You can try each possible key on the ciphertext until the result matches the plaintext

 
Modern ciphers like the Data Encryption Standard (DES) and the Advanced Encryption Standard (AES) are not so simple. Both are virtually impossible to decrypt, even using advanced computers, when a properly complex encryption key is used.  
