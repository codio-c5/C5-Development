Digital Signatures: When you sign messages digitally, the hash value of the message is encrypted instead of the message itself. This allows messages of arbitrary lengths to be signed. 
Password Files: Hashes of passwords are stored, not the passwords themselves. Because no one can see the plain password, this provides an extra layer of security in case the password file is stolen.

Slide Notes: More details on how hashes are used in digital signatures are provided in the next unit.

For password files,  a “salt” value is added to the password before hashing it. This provides protection against rainbow attacks, in which tables of hashes of possible passwords are used to compare the hashes and find the password that corresponds to the given hash. Salting makes these rainbow tables less effective. The attack can become infeasible, depending on the length of the salt. 

