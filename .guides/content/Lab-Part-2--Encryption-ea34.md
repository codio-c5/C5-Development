**Clean up any previous work**

{Cleanup}(sh rsa/cleanup.sh lab-part2)

## Upload Your Partner's Public Key

Now that you have your partner's public key (via email), you can use their public key to encrypt messages to send over a public channel, like the Internet.

**Instructor's note:** When using asymmetric key encryption (i.e., public key encryption) you use the recipient's public key to encrypt and they use their private key to decrypt.

 - In the `message.txt`file in the top left pane, write your  name and a message for your partner. 

 - Locate the public key that your partner sent you. In the tree view on the far left. Right-click on the folder `lab-part2` and click ```Upload```.
  - Once the upload is complete, click ```Close```. 
   - Click on the folder to see the file. Open the file to verify it looks like a public key.

## Provide the name of your partner's public key (optional)
If your partner has renamed their public key, then click on ```partner-pubkey.txt``` in the file tree to the left. Enter the file name of their public key in the window that opens. You can then close the tab.


## Encrypt Your Message
 - Click the encrypt button below.

{Encrypt}(sh rsa/encrypt.sh lab-part2/public.key lab-part2/message.txt lab-part2/cipher.txt)

 - Click on ```cipher.txt``` in the file tree to the left. Copy and past the encrypted output file and copy and paste the contents into the box below.

{Save!|assessment}(free-text-2646518253)


## Send an Encrypted Message
 - Download the message by right clicking on the file name and select ```Download```. 



