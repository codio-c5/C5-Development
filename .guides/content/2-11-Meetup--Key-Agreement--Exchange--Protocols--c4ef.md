## Creating Your Common Number



Pair up with a classmate.You're going to create a shared key.

Task:  Each pair will create their own key then exchange messages with another team.  
 -Paul, we need a steplist here of how they can create a key with simple arithmetic.
 (The following steps describe how to compute a trivial version of Diffie-Hellman algorithm. It demonstrates the essential aspect of D-H that enables 2 parties to generate a shared secret without directly communicating that secret. This algorithm has 2 purposes: 1. to demonstrate the general process and 2. to be easily breakable. The following lesson will use this demonstrate the actual D-H algorithm and how it works.)
  - Step 0 Pick a partner. One person will will take the role of Alice and the other Bob.
  - Step 1. Agree with your partner on a shared number and assign that number to the variable called S. For instance, pick S=3.
  - Step 2. Alice picks a number, called X1 and Bob picks a number X2. Each person keeps their number a secret. Alice assign it to the variable X1 and the other to X2. For instance, Alice picks X1=5 and Bob picks X2=4.
  - Step 3. Partner Alice plugs the shared number S=3 into the formula B=S^X1 or B equals S to the power of Alice or 3^5 = 243. Partner Bob does the same using C=S*P2 or 3^4, which eauals C=81.
  - Step 4. Alice gives the result B=243 to Bob. Bob gives the result C=81. Neither person needs to hide the exchanged numbers.
  - Step 5. Now, Alice can compute Bob's secret number by taking the Nth root of the Bob's public number C, which is 81. This is C^-S = 81^3=4. Bob does the same with Alice's  public number. Now, both Alice and Bob know each other's secret number without have transmitted the secrets to each other.
  
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
