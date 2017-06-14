![](.guides/img/acpptcryptokey.png) 

Symmetric key cryptography uses the same key for encryption and decryption. 

Alice is the sender who wants to send an encrypted message to Bob.

1. Alice has a file called `plaintext`.
1. She encrypts it using a *shared secret*, or key. You can think of this as a password for now.
1. A file called `ciphertext` is created, which she can now send to Bob.
1. Bob now needs to decrypt `ciphertext` before he can read it using the key.
1. Once, decrypted, Bob can read the original `plaintext` file sent by Alice.

The advantage of symmetric key encryption is that it is more efficient than asymmetric key encryption[^1] (which you'll learn about in Unit 2). Symmetric key encryption produces significantly less cyphertext for a given plaintext. However, the challenge with symmetric key is that getting the key to the right people and keeping it away from attackers is more difficult than for asymmetric key encryption


[^1]: Applied Cryptography, Schneier, 1996 pg.216.
