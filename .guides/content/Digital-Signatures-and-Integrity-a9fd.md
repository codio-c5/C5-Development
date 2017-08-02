|||definition 
**Data integrity** mathematically ensures that the received message has not been altered or changed. 
|||

Creating a digital signature for a message ensures its integrity during transmission. The sender first calculates a hash of a message and then encrypts the hash with the private key. The encrypted hash is sent along with the message and the hash algorithm. The recipient calculates the hash of the message and then decrypts it. If the calculated hash value matches the received (decrypted) one, then receiver knows that the message has not been altered and integrity is ensured. 
 


<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/Stylus.jpg" alt="https://commons.wikimedia.org/wiki/File% A forest of for sale signs in Oughtibridge UK.By Infrogmation of New Orleans [CC BY 2.0], via Wikimedia Commons">
  <figcaption style="font-size: 0.8em; text-align: left;"> Four  medieval styli. 
  </br>
By Numisantica [CC BY-SA 3.0], via Wikimedia Commons.</figcaption>
</figure>
<br>

## Growth Hack: Hello, It's Me
The last step in the digital signatures process is for Bob to match the hash values of the message and the digital signature. If they match, Bob knows that the message is validated. 

 


{Submit Answer!|assessment}(free-text-4200048754)
