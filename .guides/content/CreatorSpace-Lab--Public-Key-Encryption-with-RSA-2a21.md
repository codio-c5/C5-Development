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

-

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
