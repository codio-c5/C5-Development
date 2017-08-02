<figure class="snippetimg" style="margin: 0 auto;width:60%">
  <img src=".guides/img/MeetIntro.PNG">
  </figure>


## Calling All Cryptanalysts: How Would You Crack It?
What approach would you take to solve each scenario?


**1. Ciphertext-only attacks:** What do you do to break the substitution cipher if all you have is the ciphertext?

**2. Known plaintext attacks:** What do you do to break the cipher if you know that "hello" encrypts to `MYZZK`? How do you find the key?

**3. Chosen plaintext attacks:** What do you do to break the cipher if you can choose a plaintext and get its ciphertext but no key? What would you choose for the plaintext? 

**4. Chosen ciphertext attacks:** What do you do to break the cipher if you can choose a ciphertext and get its plaintext but no key? What would you choose for the ciphertext? 

|||guidance
**Instructor's Note:** As with the Meetup for shift ciphers, this works great as a Meetup.  Divide your class into groups and have each group take on one of the four scenarios. Have the groups report back to the class at large with their findings.
|||

||| guidance
**Instructor's Note:** 
**Answers** 
**Ciphertext only attacks –** Frequency analysis.
**Known plaintext attacks –** This reveals that M should be replaced by H, Y by E, L by Z, and K by O. Substitute these and see if it helps to figure out the others. Do frequency analysis if necessary.
**Chosen plaintext attacks –** Choose the whole alphabet for the plaintext.
**Chosen ciphertext attacks –** Choose the whole alphabet for the ciphertext.
|||