## Use your partner's shared key to encrypt and decrypt messages

After completing part 1, both Alice and Bob know each other's shared key without have transmitted the secrets to each other.
  
 - Enter a message to encrypt in the lower, left window or use the existing text.

 - Encrypt a message for your partner by entering the following command in the upper, left window using the shared, secret key you calculated in part 1 of this lab as the password.
 ```python aes.py encrypt message.txt cipher.txt```
 
 - Download the cipher text by first clicking dhlab-part2 in the file tree to the left. Next, right-click ```cipher.txt``` and select the Download option.
 
 - Give the message you just encrypted to your partner via email or other means, and also get their encrypted message.

- Each partner can decrypt the other's message by entering the following command in the upper, left window using the shared key.
 ```python aes.py decrypt cipher.txt orig-message.txt```
 
    Click the ```orig-message.txt``` tab next to the ```message.txt``` tab in the lower, left window to view the decrytped message.
 
 **Hint:** smaller key sizes are more vulnerable to brute-force attacks. You would use much larger prime numbers to calculate secret, shared keys in the real-world.


|||guidance
**Instructor's Note:**  This works great as a Meetup.  Divide your class into pairs and have each group explore the scenario. Have the groups report back to the class at large with their findings.
|||
