Two Belgian cryptologists - Vincent Rijmen and John Daemen -  created The Rijndael cipher in the late 1990s. (The cipher name is constructed by concatenating names and pronounced Rain-Dahl). They submitted a subset of the algorithm to the National Institute of Standards and Technology, which was conducting a search for a new encryption standard. NIST selected Rijndael as the new Advanced Encryption Standard or **AES** in 2001.  It is now used extensively worldwide, and is gradually replacing DES and 3DES.

Below is a schematic of the AES encryption algorithm. You can see from this that it is rather more rigorous in its approach than the shift and substitution algorithms we have seen so far. AES uses substitution combined with permutation that is referred to as a substitution-permutation network in cryptography. 

<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/aes.jpg" alt="Source: Figure 5.1 AES Encryption Process” <u>Cryptography and Network Security: Principles and Practice.</u> Stallings, W. ©2013 Pearson. Reprinted with permission from author.d">
  <figcaption style="font-size: 0.8em; text-align: left;"> The AES Encryption Process.
  </br>
  Source: "Figure 5.1 AES Encryption Process” <u>Cryptography and Network Security: Principles and Practice.</u> Stallings, W. ©2013 Pearson. Reprinted with permission from author.</figcaption>
</figure>

A substitution-permutation networks takes a block of the plaintext and the key as inputs, and applies several alternating "rounds" or "layers" of substitution boxes (S-boxes) and permutation boxes (P-boxes) to produce the `ciphertext` block. The S-boxes and P-boxes transform (sub-)blocks of input bits into output bits. It is common for these transformations to be operations that are efficient to perform in hardware, such as exclusive or (XOR) and bitwise rotation. The key is introduced in each round, usually in the form of "round keys" derived from it (In some designs, the S-boxes themselves depend on the key).