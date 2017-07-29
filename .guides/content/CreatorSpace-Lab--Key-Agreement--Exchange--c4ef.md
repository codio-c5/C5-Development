## Creating Your Common Numbers

Pair up with a classmate. You're going to create a shared key using the Diffie-Hellman Key Exchange algorithm. This algorithm enables two parties to generate a shared secret without directly communicating that secret. 
    
1. **Pick a partner.** One person will will take the role of Alice and the other is Bob.
1. **Agree on two non-secret numbers.** Agree with your partner on two shared numbers, $P$ and $G$.  They must be prime numbers.
  Here are a few prime numbers to use for $P$ and $G$: 
  ```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...
  ```
  For example, pick $P=23$ and $G=5$.
  
**1. Choose a private number.** Alice picks a number, called $A$ and Bob picks a number $B$. Each person keeps their number a secret. For instance, Alice picks $A=6$ and Bob picks $B=15$.

**2. Calculate the public (shared) key.**
 -  **Alice calculates.** If you are Alice, enter the following command in the terminal window, the upper left pane:

```python dh.py 23 5 6```

 - Alice plugs the shared numbers $P$ and $G$ into the formula, $X = G^A mod P$. 
 In plain English, $X$ equals $G$ multiplied by itself $A$ times and then divided by $P$ keeping only the remainder. Using the example values: $5*5*5*5*5*5 = 15625$ and then $15625  mod  23 = 8$.

 - **Bob calculates.** If you are Bob, enter the following command in the the terminal window, the upper left pane:
 
```python dh-pubkey.py 23 5 15```

Partner Bob does the same using $X = G^A mod P$ or $5^{15} mod 23$ and the answer becomes $X=19$.

**3. Exchange results.**  Alice gives the result $X=8$ to Bob. Bob gives the result $Y=19$ to Alice. You don't have to hide the exchanged numbers.

**4. Calculate the private key.**

 - **Alice generates her secret key.** Alice can now generate her shared secret using the value Bob provides, and the original numbers **23** and **5**:

In the left pane, enter your partner's public key at the prompt.

Alice gets the number **2**.

 -  **Bob calculates his secret key.** Bob can do the same. He generates his secret using the value Alice provides, and the original numbers **23** and **5**. 
 
In the terminal window in the upper left pane, enter your partner's public key at the prompt.

Bob gets the number **2**.

**5. Crack your partner's key.**

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
