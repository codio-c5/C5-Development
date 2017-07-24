## Creating Your Common Numbers

Pair up with a classmate. You're going to create a shared key using the Diffie-Hellman Key Exchange algorithm. This algorithm enables two parties to generate a shared secret without directly communicating that secret. 
    
1. **Pick a partner.** One person will will take the role of Alice and the other Bob.
1. **Agree on two non-secret numbers.** Agree with your partner on two shared numbers, ``P`` and ``G`` must be prime numbers and ``P`` must be greater than ``G``.
    For the first time experimenting this lab, both Alice and Bob should use the following numbers ``P=23`` and ``G=5``.
  
    The next time through you can use the following prime numbers for ``P`` and ``G``: ``2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97``

1.  **Choose a private number.** Alice picks a number, called ***A*** and Bob picks a number ***B.*** Each person keeps their number a secret. For instance, Alice picks ``A=6`` and Bob picks ``B=15``.
1. **Now, let's do the first calculation that will determine the shared number**

    **Alice calculates.** If you are ``Alice``, enter the following command in the window to the left:

    ``python dh.py 23 5 6``

    Alice plugs the shared numbers "P" and "G" into the formula, X = G^A mod P. In plain English, X equals``G`` multiplied by itself ``A`` times and then divided by "P" keeping only the remainder. Using the example values: ``5*5*5*5*5*5 = 15625`` and then ``15625 mod 23 = 8``.

    **Bob calculates.** If you are "Bob", enter the following command in the window to the left:

    ``python dh-pubkey.py 23 5 15``

    Partner Bob does the same using ``X = G^A mod P`` or ``5^15 mod 23``, and ``X=19``. In this case, the answer is ``19``.

1.  **Alice gives the result** ``X = 8`` to Bob. Bob gives the result ``Y = 19`` to Alice. Neither person needs to hide the exchanged numbers.

1.  **Alice generates her secret key** Alice can now generate her shared secret using the value Bob provides and the original numbers ``23`` and ``5``:

Enter your partner's public key at the prompt

Alice gets the number ``2``

1.  **Bob calculates his secret key** Bob can do the same:

Now, Alice can compute Bob's secret number by taking the n^th^ root of the Bob's public number y, which is 81. This is ``y^-s^= 81^3^=4``. Bob does the same with Alice's  public number. Now, both Alice and Bob know each other's secret number without have transmitted the secrets to each other.

Now you have a shared key with your partner.  

 - Encrypt a message to your partner.
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
