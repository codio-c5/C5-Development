##       Unit Check In

### Cryptographic hash functions solve the problem of integrity by providing a hash value (also known as a  message digest) used to verify that a message has not been tampered with. 

Hash functions are used for digital signatures, password files, intrusion and virus detection, pseudorandom number generation, and file synchronization.

No matter how long a message is, a hash function produces a fixed size **hash value.**  The size is a compression of the original plaintext, which makes hash values as easy to store and transmit as they are fast and easy to calculate. 

A hash function is **pre-image resistant.** It is a one-way process in which the original message cannot be determined from the hash value. 

In a cryptographic hash function, the same message always yields the same hash value, and different messages, no matter how similar, always yield a unique hash value.  The unique values are considered **collision resistant.** 

Since brute force attacks on hash values are too time-consuming, the more common forms is a **collision attacks** where cryptanalysts seek different messages that yield the same hash values.

