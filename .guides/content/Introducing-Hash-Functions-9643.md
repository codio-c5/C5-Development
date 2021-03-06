Cryptographic hash functions help solve the problem of integrity. The algorithm is one-way, meaning that it can be encrypted but not decrypted, so it is useful in validating the sender and the integrity of the message.

|||definition
A cryptographic **hash function** is an algorithm that produces a condensed encryption of a message that can be verified as authentic, or **digitally signed.** 
|||


<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/Hashfn.PNG" alt="A hash function">
  <figcaption style="font-size: 0.8em; text-align: left;">A hash function.   
  </figure>
  
A cryptographic hash function produces a **hash value** or **message digest** that cannot be decrypted back into the original plaintext.  A hash value is compressed to a specific size data set, no matter what the length of the plaintext. Because it is short, it is easy to store and send.  

Another key property of a cryptographic hash function is that it is nearly impossible to find two different messages that have the same hash value. A **collision** occurs when two messages have the same hash value.

|||guidance
**Instructor's Note:** Note that hash functions are not encryption functions (although you’ll hear many people say “encrypted” for “hashed” data). The reason hashes are not encryptions is because the original data cannot be recovered from the hash value. Indeed, it is one of the requirements of the hash functions that the hash value cannot be inverted (pre-image resistance).
|||

