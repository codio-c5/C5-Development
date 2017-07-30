The ROTate by 13 places cipher (ROT13) is another instance of a shift cipher. It shifts each character 13 places, or half-way through the Latin (i.e., English) alphabet. This is not an arbitrary choice because the ROT13 cipher will encrypt a plaintext message the first time it is applied, and it will decrypt the resulting ciphertext the second time it is applied. It's like moving the hour hand of a clock forward 6 hours and then forward again by 6 hours and ending up where you started. If you use a cipher with a key other than 13, applying the cipher to the ciphertext that resulted from the first shift won't bring back the original plaintext. The second application of the cipher will just result in more ciphertext. Only key=13 lets you jump from plaintext to ciphertext and back to plaintext in just two applications of the key. 

  <img src=".guides/img/ROT13.png" alt="“ROT13 table with example” By Benjamin D. Esham derived from “ROT13.png” by Matt Crypto. 
 Public Domain.">
  <figcaption style="font-size: 0.8em; text-align: left;">ROT13 table with example. By Benjamin D. Esham derived from ROT13.png by Matt Crypto. 
  <br>
 Public Domain. </figcaption>
</figure>



The interactive ROTn Shift Cipher tool in the left panel is an cryptanalyst tool that lets you experiment with decoding ciphertext. It applies all 25 possible keys (or rotations) to any ciphertext you enter.

- Enter the ciphertext `WDNH PH RXW WR WKH EDOO JDPH` in the main text area.
 - Click `Show ROTn`.
 - Examine the results to see whether something stands out. (Hint: Look towards the bottom.)

You just used the **brute force** cryptanalysis technique by using a tool that tries every possible key to reveal the plaintext.

## On Your Own
Enter different shift-created ciphertexts and use the tool to practice decrypting them. In other words, write some plaintext, choose a key, create ciphertext using that key, enter the ciphertext, and watch the tool apply all the keys so as to reveal your original plaintext. 
