In this three-part lab, you break into pairs or small groups. You will then use RSA to complete the following steps:

1. Each individual or group will generate a key pair.
1. You then share your public key with your partner and vice versa.
1. Using your private key, encrypt a message
    They do the same using their message private key.
1. Send your ciphertext to your partner.
    Your partner send you their ciphertext.
1. Use your partner's public key to decrypt their message
    They decrypt your message using your private key.

Compare results.

Optionally, you can reverse the process:
1. Encrypt your partner's plaintext using your private key again.
    Your partner does the same with your plaintext.
1. Decrypt the ciphertext using your partner's public key.
    Your partner does the same.
    
Each should get their original plaintext back.

Click the clean up button to clear out any previous work.
{CLEAN UP}(sh rsa/cleanup.sh lab-part1)

## Generate Your Keys

To get started, you will generate a key pair; your partner will do the same. A key pair consists of a private key and a public key.

Click the Generate keys button.

{Generate keys}(sh rsa/keygen.sh) 

The file tree on the left shows the keys, along with other files, that you just generated. One is ```private.key``` and the ```public.key```.

 - Click on the private key in the file tree, on the left, and a tab opens in this space showing its contents. (You can move between the tabs by clicking on them.)
 - Copy and paste the private key into the box below. 
 {Submit Answer!|assessment}(free-text-3445674952)

 - Open up the public key file that has been created.
 - Copy and paste the public key into the box below. 
 {Submit Answer!|assessment}(free-text-648952340)
 
## Download The Public Key

 - Download the public key file. To download, right click on the public key file name in the tree on the left and select "Download". 

## Rename and Email Public Key

- You and your partner(s) will be exchanging public keys - in order to avoid confusion later in the unit, we recommend you rename your file (that you just downloaded) by adding your name to the file name. e.g. ```Steve_public.key```

- Now email the renamed public key file to your partner

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
