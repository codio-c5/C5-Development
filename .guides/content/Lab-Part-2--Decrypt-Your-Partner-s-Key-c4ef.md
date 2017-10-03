## Use your partner's shared key to encrypt and decrypt messages

After completing part 1, both Alice and Bob know each other's secret number without have transmitted the secrets to each other.
  
 - Enter a message to encrypt in the lower, left window or use the existing text.

 - Encrypt a message for your partner by entering the following command in the upper, left window using the shared, secret key you calculated in part 1 of this lab as the password.
 ```python aes.py encrypt message.txt cipher.txt```
 
 - Download the cipher text by first clicking diffiehellman/lab-part2 in the file tree to the left. Next, right-click ```cipher.txt``` and select the Download option.
 
 - Give the encrypted message to another team, and take a message they have encrypted using their shared key.

- Each team can decrypt the other team's message by entering the following command in the upper, left window using the shared, secret key.
 ```python aes.py decrypt cipher.txt orig-message.txt```
 
    Click the ```orig-message.txt``` tab next to the ```message.txt``` tab in the lower, left window.
 
 **Hint:** smaller key sizes are more vulnerable to brute-force attacks. You would use much larger prime numbers to calculate secret, shared keys in the real-world.


|||guidance
**Instructor's Note:**  This works great as a Meetup.  Divide your class into pairs and have each group explore the scenario. Have the groups report back to the class at large with their findings.
|||
