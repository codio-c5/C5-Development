## Crack your partner's key

Now, Alice and Bob can compute each other's secret number.
Alice takes the n^th^ root of the Bob's public number $y$, which is 81. This is ```y^-s^= 81^3^=4```. 
Bob does the same with Alice's  public number. Now, both Alice and Bob know each other's secret number without have transmitted the secrets to each other.
  
Now you have a shared key with your partner.

 - Enter a message to encrypt in the lower, left window or use the existing text.

 - Encrypt a message to your partner by entering the following command (enter your private key as the password):
 ```python aes.py encrypt message.txt cipher.txt```
 
 - Click the output file name, ```cipher.txt```, in the file tree on the far left. It will be displayed in a new tab in the lower, left window.
    
 - Give the encrypted message to another team, and take a message they have encrypted using their shared key.
 - Try to decrypt the other without their key
 ```python aes.py decrypt cipher.txt orig-message.txt```
 
    Click on the output file ```diffiehellman/orig-message.txt``` in the file tree to the left.
 
 **Hint:** smaller key sizes are more vulnerable to brute force attacks.

 - If you weren't successful, try again using their key.


|||guidance
**Instructor's Note:**  This works great as a Meetup.  Divide your class into pairs and have each group explore the scenario. Have the groups report back to the class at large with their findings.
|||
