Intrusion/Virus Detection: A change in the hash value of a file may indicate an intrusion or a virus.
Construction of a pseudorandom number generator: One of the required properties of a cryptographic function is that the output has to pass pseudorandomness tests.
File synchronization: Whether to upload a file or not for synchronization (for example with the cloud storage) can be determined by checking the hash value of the file has changed or not since the last update

Slide Notes:
Hash functions can be used for intrusion detection and virus detection. This is done by storing the hash of the file for each file on a system and securing the hash values (e.g., on a flash drive that is kept secure). One can later determine if a file has been modified (by a virus or someone else) by recomputing
the hashes and comparing them with the secured hash values. An intruder would need to change the hash value of a file without changing the file itself to hide his/her actions. However, the collision resistance property makes it very hard for the intruder to make such a change.

A cryptographic hash function can be used to construct a pseudorandom function (PRF) or a pseudorandom number generator (PRNG), the output from a hash need to pass tests for pseudorandomness.
