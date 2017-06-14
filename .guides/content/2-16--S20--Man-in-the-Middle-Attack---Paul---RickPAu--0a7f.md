
Taught as animation

with voice over

 

In this diagram, Alice and Bob want to agree on a key. They first share their public keys. This is where the evil Man-in-the-Middle, EVE, comes into the picture. She intercepts Alice’s public key and sends Bob her own public key instead. She also intercepts Bob’s public key and sends Alice her own public key.

Now Alice and Bob both calculate keys using the public keys they receive and their own private keys. They think they are calculating the same key as one another but indeed what they calculate can only be calculated by Eve. Eve calculates the two keys, one with Alice’s public key and one with Bob’s public key, and communicates with Bob as if she is Alice and communicates with Alice as if she is Bob. Alice and Bob have no idea that their messages are read by and possibly modified by Eve.

The key exchange protocol is vulnerable to such an attack because it does not authenticate the participants. This vulnerability can be overcome with the use of digital signatures and public key certificates.

