The Caesar cipher is an ancient *(Hail Caesar!)* and simple form of encryption known as shift ciphers. A shift cipher takes each character of a text message and then shifts each letter in the message N letters to the right in the alphabet. The version known as the Caesar cipher specifically shifts 3 letters to the right.  

### Example of a Caesar Cipher
In the following example, the *key* is 3. Each letter is shifted 3 letters to the right in the alphabet.

```
meet me after the toga party
phhw ph diwhu wkh wrjd sduwb
```

Notice how the last N letters (3 in the above example) are dealt with by starting again at the letter "a" if it would go past "z".

If you know a ciphertext is obtained using Caesar Cipher, getting the original plaintext is simple. You can just try different keys until you find the one that works. Solving a cipher is called  *cryptanalysis*. Solving by trying different combinations is call a *brute force attack*.