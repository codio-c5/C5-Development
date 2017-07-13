## Pass the Salt, Please
**Password Files.** Websites store hashes of passwords,not the passwords themselves. This provides an extra layer of security in case the password file is stolen, because of the one-way nature of the hash value. A **salt** value is a randomly generated number that is added to the password before hashing it, to provide protection against **rainbow attacks.** 

<figure class="snippetimg" style="margin: 0 auto;width:80%">

  <img src=".guides/img/Salt.jpg" alt="Public key cryptography inventors Whitfield Diffie and Martin Hellman. . *Source: Whitfield Diffie photo by Mary Holzer licensed under CC-BY and Martin Hellman originated from Martin Hellman licensed under GFDL.*
">
  <figcaption style="font-size: 0.8em; text-align: left;">Salt shakers.
</br>
 © Jorge Royan / http://www.royan.com.ar, licensed under the Creative Commons Attribution-Share Alike 3. via Wikimedia Commons</figcaption>
</figure>


|||definition
**Rainbow attacks** use large **rainbow tables** or **dictionaries** that pair hash values with possible passwords. The hacker compares the hashes to find its corresponding password. 

**Salting** makes hash values exponentially harder to break. Each bit of salt doubles the computation, and  the attack can become infeasible.
|||