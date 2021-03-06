Once you receive your partner's encrypted message, follow these steps to decrypt it.

## Decrypt The Message

- If you are ```Alice```, click the ```Alice decrypts Bob's ciphertext``` button.

{Alice decrypts Bob's ciphertext}(sh rsa/decrypt.sh alice-private.key cipher.txt partner-message.txt)

- If you are ```Bob```, click the ```Bob decrypts Alice's ciphertext``` button.

{Bob decrypts Alice's ciphertext}(sh rsa/decrypt.sh bob-private.key cipher.txt partner-message.txt)

Your partner's message should be visible in the panel to the left. (If it is not, then click on the lab-part3/partner-message.txt file in the file tree to the left.)

 - Open the output file and copy and paste the contents into the box below.

{Save!|assessment}(free-text-3356212759)

You can try the process again with other partners.

**Optional:** You can repeat part 2 and encrypt your partner's message using their public key and send the ciphertext to them. They should be able to decrypt their original message using their private key.
