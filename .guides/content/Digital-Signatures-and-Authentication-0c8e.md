If encrypted with a private key,  the successful decryption of a ciphertext with the corresponding public key indicates that the message was indeed encrypted with the private key that corresponds to the public key used for decrypting it.

So if we consider the ciphertext of the message as a signature, then the successful decryption indicates a verification of the signature.

In practice, the hash value of the message is encrypted to get the signature, not the message itself. (Recall that a message can be arbitrarily large but the hash value has a fixed length.)
