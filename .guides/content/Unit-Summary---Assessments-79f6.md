##       Unit Check In

### Public key cryptography solves the problem of shared key distribution by separating the process of encryption from decryption. Users create a key pair and share a public key that senders can use to encrypt messages. Only the message recipient has the private key necessary to decrypt messages sent to them.

Common methods of public key encryption include **RSA** encryption and **elliptic curve cryptography (ECC).**  RSA relies on the factoring of two large prime numbers, and ECC uses the pairing of points on an elliptical curve.  

**Key agreement algorithms** are another form of public key cryptography. Also known as **key exchange algorithms,** the sender and recipient exchange **public keys** and generate a shared value using their **private keys.** This shared value, known as a **session key,** is used both to encrypt and to decrypt messages between the two parties. 

Although it's more secure than symmetric key cryptography, public key cryptography is still vulnerable to issues of **authenticity** and **integrity,** as described in the **man-in-the-middle attack.**
