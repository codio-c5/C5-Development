The ROTate by 13 places cipher (ROT13) is variation of the shift cipher. It shifts each character 13 places, or mid-way through the Latin (i.e., English) alphabet. This is not an arbitrary choice because the ROT13 cipher will encrypt a plaintext message the first time it is applied, and decrypt the ciphertext the second time it is applied. It's like moving the hour hand of a clock ahead 6 hours and then forward again by 6 hours and ending up where you started.

  <img src=".guides/img/ROT13.png" alt="“ROT13 table with example” By Benjamin D. Esham derived from “ROT13.png” by Matt Crypto. 
 Public Domain.">
  <figcaption style="font-size: 0.8em; text-align: left;">ROT13 table with example By Benjamin D. Esham derived from ROT13.png by Matt Crypto. 
  <br>
 Public Domain. </figcaption>
</figure>


As we've learned shift ciphers provide only the most basic encryption. However, the ROT13 cipher is still a useful tool. It can be used to hide information like plot spoilers on movie review websites. It's also good for teaching introductory cryptography.

The interactive ROTn on the left hand side is an cryptanalyst tool that lets you experiment with decoding ciphertext. It applies all 26 possible keys to the ciphertext.

Enter some ciphertext, for instance like  `WDNH PH RXW WR WKH EDOO JDPH`, in the main text area and then press `Show ROTn`.

The application applies all 26 possible keys - rotations - to the ciphertext. Examine the results and see if something stands out.

**Hint:** look towards the bottom.
{Submit Answer!|assessment}(free-text-3117283162)

You just used the **brute force** cryptanalysis technique by trying every possible key. 
|||guidance
**Instructor's Note:** When ROT13 is applied twice to a message, you get the message back because of 13 being the number of the middle character in the alphabet. 

Plaintext   -->  Ciphertext  --> Plaintext
|||
