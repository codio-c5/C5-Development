The Caesar Cipher is an ancient *(Hail Caesar!)* and simple form of encryption that belongs to the class of shift ciphers. A shift cipher takes each character of a text message and then shifts each letter in the message `n` letters to the right in the alphabet. The version known as the Caesar Cipher  shifts each letter three letters to the right in the alphabet. For example, an "a" becomes a "d" when you're using this cipher. 

### Example of a Caesar Cipher
Because we're looking at a message created using the Caesar Cipher, we know that the *key* here is 3—each letter is shifted three characters to the right.

```bash
Plaintext:  meet me after the toga party
Ciphertext: PHHW PH DIWHU WKH WRJD SDUWB
```



The last `n` letters of the alphabet (3 in the case of the Caesar Cipher) are dealt with by starting again at the letter "a" if the letter must go past "z" to complete its three-letter shift. In this example, the plaintext "y" in "party" becomes ciphertext "b" after the shift.

If you know that ciphertext was created by using a shift cipher, getting the original plaintext is simple. You just try different keys—1 for a one-letter shift, 2 for a two-letter shift, 3, 4, etc.—until you find the one that produces an intelligible message. 

||| definition 
 Solving a cipher is called  **cryptanalysis.**

Solving a cipher by trying different combinations, one after another after another, to determine the key is called a **brute-force attack.** A brute-force attack is a specific kind of cryptanalysis technique, in other words.
|||

## Knowledge Check in 
{Check It!|assessment}(fill-in-the-blanks-3769728457)
