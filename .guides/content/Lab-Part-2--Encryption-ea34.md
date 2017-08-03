In part 1, you generated a public and private key pair and obtained your partner's public key via email.

## Upload Your Partner's Public Key

If you are Bob, you will use Alice's public key (alice-public.key); Alice will use Bob's public key (bob-public.key)

 - Right-click on ```lab-part2``` and select the ```Upload``` option from the menu.
 
 - Select the ```Upload...``` option from the Upload file dialog. 
 The UPLOAD FILES dialog opens
 
 - Click the ```Browse For Files``` option in the dialog
 Another Dialog opens showing files on your computer, including the public key file that you just downloaded.
 
 - Click on the public key file (e.g., alice-public.key or bob-public.key that you received from your partner and select Open

 - Click the ```CLOSE``` button in the UPLOAD FILES dialog.

You should see your partner's public key in the lab-part2 folder in the file tree on the left. Now you can use you partner's public key to encrypt messages to send over a public channel, like the Internet.

**Instructor's note:** When using asymmetric key encryption (i.e., public key encryption) you use the recipient's public key to encrypt and they use their private key to decrypt.

## Create a message

 - In the `message.txt`file in the top left pane, write your name and a message for your partner.

## Encrypt Your Message

- If you are ```Alice```, click the Encrypt Alice's message with Bob's public key button.

{Encrypt Alice's message with Bob's public key}(sh rsa/encrypt.sh bob-public.key message.txt cipher.txt)

- If you are ```Bob```, click the Encrypt with Alice's public key button.

{Encrypt Bob's message with Alice's public key}(sh rsa/encrypt.sh alice-public.key message.txt cipher.txt)

 - Click on ```cipher.txt``` in the file tree to the left. Copy and past the encrypted output file and copy and paste the contents into the box below.

{Save!|assessment}(free-text-2646518253)


## Send an Encrypted Message
 - Download the message by right clicking on the file name and select ```Download```. 



