## Create Public and Shared (Private) Keys

Pair up with a classmate. You're going to start by calculating a public key and a private key using the Diffie-Helman Key Exchange protocol. Then you will exchange the public key with your partner.

1. **First, ensure a uncluttered working environment.** 
{Cleanup}(sh /home/codio/workspace/diffiehellman/cleanup.sh)
1. **Pick a partner.** One person will will take the role of Alice and the other is Bob.
1. **Agree on two non-secret numbers.** Agree with your partner on two shared numbers, $P$ and $G$.  They must be prime numbers.
  Here are a few prime numbers to use for $P$ and $G$: 
  ```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...
  ```
  For example, pick $P=23$ and $G=5$.
  
**1. Choose a private number.** Alice picks a number, called $A$ and Bob picks a number $B$. Each person keeps their number a secret. For instance, Alice picks $A=6$ and Bob picks $B=15$.

**2. Calculate the public (shared) key.**
 -  **Alice calculates.** If you are Alice, enter the following command in the terminal window in left pane:

```python dh.py 23 5 6```

 - Alice plugs the shared numbers $P$ and $G$ into the formula, $X = G^A mod P$.
 In plain English, $X$ equals $G$ multiplied by itself $A$ times and then divided by $P$ keeping only the remainder. Using the example values: $5*5*5*5*5*5 = 15625$ and then $15625  mod  23 = 8$.
 
 - Alice's public key is 8 in this example.

 - **Bob calculates.** If you are Bob, enter the following command in the the terminal window, the upper left pane:
 
```python dh.py 23 5 15```

Partner Bob does the same using $X = G^A mod P$ or $5^{15} mod 23$ and the answer becomes $X=19$.

 - Bob's public key is 19 in this example.

**3. Exchange results.**  Alice gives the result, her public key, $X=8$ to Bob. Bob gives the result, his public key, $Y=19$ to Alice. You don't have to hide the exchanged numbers.

**4. Calculate the private key.**

 - **Alice generates her secret key.** Alice can now generate her shared secret using the value Bob provides, and the original numbers **23** and **5**:

In the left pane, enter your partner's public key at the prompt.

Alice calculates the number **2**.

 -  **Bob calculates his secret key.** Bob can do the same. He generates his secret using the value Alice provides, and the original numbers **23** and **5**. 
 
In the terminal window in the upper left pane, enter your partner's public key at the prompt.

Bob calculates the number **2**.
