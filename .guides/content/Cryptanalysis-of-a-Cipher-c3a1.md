## How Do You Crack a Code?

A cryptanalyst first needs to know what information he has before creating a decoding strategy. The elements of a code are these: the original plaintext, the resulting ciphertext, and the encryption/decryption key. To crack a code, your strategy depends on what you have. 

Following Kerckhoffs’s Principle, let's assume that the details of the algorithm used for encryption is known. If you know the key, you can simply convert plaintext or ciphertext with ease.
 

## Getting Forceful 
As you've seen, for simple ciphers like the Caesar cipher, you can use **brute force** to find the key. You test each possible key until you find the plaintext. 
||| definition
**Brute force** is the method of solving for the key by testing each possibility until you find the key.
|||
Start with ```key=1```, shift the letters of the first ciphertext "word" by that amount, and look at the result. If the result is recognizable, you might have found the key. In that case, you would decrypt the second ciphertext word using the same key. If it too is recognizable, you have likely indeed found the key. If not, try ```key=2``` and continue from there.  You know there are only 25 possible keys in a shift cipher for English, so you can complete the process quickly even without a computer.

||| guidance
**Instructor's note:**  When the Caesar Cipher shifts past the end of the alphabet, it cycles back to the beginning and continues the count specified by the key. You can also think of the alphabet as a circle where each letter has a numeric position and there is no beginning nor end. When you use that concept you enter into the world of modular arithmetic. In Modular Arithmetic the alphabet has a Modulus of 26.
https://en.wikipedia.org/wiki/Modular_arithmetic
That shift ciphers like Caesar use modular arithmetic is probably interesting only to those with a mathematical background. However, modular arithmetic is the basis for ciphers like RSA.
|||

If you have **knowntext,** which is a pairing of both the plaintext and the ciphertext, the cryptanalysis process is much easier. You would follow the above algorithm until you quickly discover the key. For example, if you had "meet" plaintext and  `QIIX` ciphertext, you would fairly quickly discover that ```key=4``` brings the texts into alignment. There's no guessing whether a key is correct because the decrypted ciphertext will either match the plaintext or not. In this example, ```key=4``` is the only key that makes the texts match.

Notice that you can discover a key by searching in either direction. You can take plaintext and apply a  key to see whether the result matches the ciphertext. (This process is the basis for cracking passwords.) Or you can work from the ciphertext to see whether the key gets you to the plaintext.

You can still find the key if you have only part of the plaintext. For example, you might have ciphertext `XPPE XP LQEPC ESP EZRL ALCEJ` but only "party" for plaintext. The only ciphertext strings of five letters are `LQEPC` and `ALCEJ`. You can try each possible key on these two ciphertext strings until the result matches the plaintext word "party". Once you have the key, you can apply it to the rest of the ciphertext to reveal the rest of the plaintext.

Later, you'll learn about modern ciphers like the Data Encryption Standard (DES) and the Advanced Encryption Standard (AES), which are not simple at all. Both are virtually impossible to decrypt when a properly complex encryption key is used, even by advanced computers.  
