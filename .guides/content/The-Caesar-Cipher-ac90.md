The Caesar cipher is an ancient *(Hail Caesar!)* and simple form of encryption that belongs to the class of shift ciphers. A shift cipher takes each character of a text message and then shifts each letter in the message `n` letters to the right in the alphabet. The version known as the Caesar cipher specifically shifts 3 letters to the right.  

### Example of a Caesar Cipher
In the following example, the *key* is 3. Each letter is shifted 3 letters to the right in the alphabet.

```bash
Plaintext:  meet me after the toga party
Ciphertext: PHHW PH DIWHU WKH WRJD SDUWB
```



Notice how the last `n` letters (3 in the above example) are dealt with by starting again at the letter "a" if it would go past "z".

If you know a ciphertext is obtained using a shift cipher, getting the original plaintext is simple. You can just try different keys until you find the one that produces an intelligible message. 

||| definition 
 Solving a cipher is called  **cryptanalysis.**
 Solving a cipher by trying different combinations to determine the key is call a **brute force attack.**
|||

## Knowledge Check in 
{Check It!|assessment}(fill-in-the-blanks-3769728457)