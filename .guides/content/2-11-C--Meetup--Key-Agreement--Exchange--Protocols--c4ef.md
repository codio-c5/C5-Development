## Creating Your Common Number



Pair up with a classmate. You're going to create a shared key using the Diffie-Hellman Key Exchange algorithm. This algorithm enables two parties to generate a shared secret without directly communicating that secret. 

1. **Pick a partner.** One person will will take the role of Alice and the other Bob.
1. **Agree on a shared secret.** Agree with your partner on a shared number, "s". For example, pick s=3.
1.  **Choose a private number.** Alice picks a number, called ***a*** and Bob picks a number ***b.*** Each person keeps their number a secret. For instance, Alice picks a=5 and Bob picks b=4.
1.  **Alice calculates.** Partner Alice plugs the shared number s into the formula x=s^a^.  In plain English, x equals s to the power of a. Using the example values:3^5^ = 243. 
1. **Bob calculates.** Partner Bob does the same using y=s^b^ or 3^4^, or y=81.
1.  Alice gives the result x=243 to Bob. Bob gives the result y=81. Neither person needs to hide the exchanged numbers.
1.  Now, Alice can compute Bob's secret number by taking the n^th^ root of the Bob's public number y, which is 81. This is y^-s^= 81^3^=4. Bob does the same with Alice's  public number. Now, both Alice and Bob know each other's secret number without have transmitted the secrets to each other.
  
Now you have a shared key with your partner.  

 - Encrypt a message to your partner.
 
 U
 - Give the encrypted message to another team, and take a message they have encrypted using their shared key.
 - Try to decrypt the other without their key
 - If you weren't successful, try again using their key.



 

• Public Key Cryptography gives us another way to communicate privately without having to share secret information prior to the communication.


•Purpose is to enable two users to securely agree on a key that can then be used for subsequent symmetric encryption of messages.



*What approach you would take to solve each scenario?*


*
|||guidance
**Instructor's Note:**  This works great as a Meetup.  Divide your class into pairs and have each group take on one of the four scenarios. Have the groups report back to the class at large with their findings.
|||
