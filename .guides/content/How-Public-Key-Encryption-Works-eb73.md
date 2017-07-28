

<div>
  <iframe src="//player.vimeo.com/video/222887386" width="500" height="330" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>

<br>
## How it works:
 - Each user generates a pair of keys that consist of a public and a private key.  
 - The users share their public keys, but they keep their private key to themselves.
 - The sender encrypts her message with the receiver's public key to create a ciphertext she can send to the receiver.
 - The receiver is able to decrypt the ciphertext by using his private key. 
 - The receiver can then send a response by encrypting the plaintext using the initial sender's public key.
 - The initial sender can then decrypt the return message by using her private key.
 
## Advantages and Disadvantages
Because users share only a public key used for encryption, keeping key distribution safe and a secret is not an issue. Public keys can be broadly shared over non-secure channels and used by others to encrypt messages for the key's creator. Only the key's creator has the private key that can be used to decrypt messages encrypted with their public key.

Public key encryption is significantly more computationally expensive, and it requires more storage than symmetric key encryption. This is typically an acceptable trade-off today, given high-speed computer processing and the importance of confidentiality.


 



