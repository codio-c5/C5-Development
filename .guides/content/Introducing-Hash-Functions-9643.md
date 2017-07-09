A hash function maps digital data of arbitrary size to digital data of fixed size. The hash is sometimes called a message digest.

A cryptographic hash function is a hash function that is considered practically impossible to invert (one-wayness) or find collisions (i.e. two messages with the same hash value).

Illustration from S7

For a regular hash function, inversion is not a concern, but for a cryptographic hash function it is an essential property.

Slide notes:Note that hash functions are not encryption functions (although you’ll hear many people say “encrypted” for “hashed” data). The reason hashes are not encryptions is because the original data cannot be recovered from the hash value. Indeed, it is one of the requirements of the hash functions that the hash value cannot be inverted (pre-image resistance).
