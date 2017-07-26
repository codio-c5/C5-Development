In this lab activity you will pair with a classmate and send each other encrypted messages.

To start, [click here](cmd ./cleanup.sh) to clean up any previous work.

**Part 1: Generate Keys**

On the left is a Linux terminal window. We will first of all enter a command to create a private/public key pair.
Generate key pair

To generate a private/public key pair, [Click here](cmd ./keygen.sh private.txt public.txt) to run the command below

```keygen.sh private.txt public.txt```

Once you have done this, click on the folder name rsa/lab-part1 in the file tree on the left open up the private key file that has been created.

Copy and paste the contents into the box below. Do the same for the public key, pasting it below the private key.

{Save|assessment}(free-text-1209885361)
Send the public key

You should now download the public key file and send it to your partner via email. To download, right click on the public key file name in the tree on the left and select "Download".

In order to avoid confusion later in the unit, we recommend you rename your file by adding your name to the file name. e.g. Steve_public.txt

**Part 2: Encrypt message**

Upon receiving your partners public key via email, you can send encrypted messages to him/her over a public channel (the Internet).

On the left we have opened up a file message.txt. Write your full name and a message for your partner in this file.
Upload partner's public key

You should now locate the public key that your partner sent you. In the tree view on the left hand side, right-click on the folder lab-part2 and then press Upload.

Upload the file now. Once the upload is complete, press the Close button. Click on the folder to see the file and open the file to verify it looks like a public key.
Encrypt

You are now ready to encrypt your message. In the terminal window on the left, encrypt your message with the following command [Click here](cmd ./encrypt public_key_file_name message.txt encrypted_file_name) to run the command below

```encrypt public_key_file_name message.txt encrypted_file_name```

Be sure to specify your partners public key file name correctly and a valid output file name.

Once you are done, open up the encrypted output file and copy and paste the contents into the box below.

{Save|assessment}(free-text-2661247406)
Send encrypted message

You are now ready to send your encrypted file to your partner. To download it, right click on the file name in the tree on the left and select "Download".

**Part 3: Decrypt message**

Upon receiving your partners encrypted message for you, we can now decrypt it.
Upload partner's public key

You should now locate the encrypted file that your partner sent you. In the tree view on the left hand side, right-click on the folder lab-part1 and then press Upload.

Upload the file now. Once the upload is complete, press the Close button. Click on the folder to see the file and open the file to verify it looks like an encrypted file.
Decrypt it

You are now ready to decrypt the message. Bring back the terminal window (you will see its tab in the top of the main panel to the left.)

You can now decrypt your message with the following command [Click here](cmd ./decrypt private_key_file_name encrypted_file_name decrypted_file_name)

```decrypt private_key_file_name encrypted_file_name decrypted_file_name```

Be sure to specify the file names correctly.

Once you are done, open up the encrypted output file and copy and paste the contents into the box below.

{Save|assessment}(free-text-1959244157)


# Parts 1-5 to be integrated from Ian's GH posting of the same title.
Accompanying stack needs to be pointed to as well.

|||guidance
**Instructor's Note:**

Grading Rubric
| Item | Max points |
|-|-|
| Part 1: Key Generation |	20 |
| Part 2: Encryption |	20 |
| Part 3: Decryption |	20 |
| Answers to 2 questions	| 20 |
| Style	|10 |
| Answers to reflection questions	| 10 |
| **Total** | **100** |
|||
