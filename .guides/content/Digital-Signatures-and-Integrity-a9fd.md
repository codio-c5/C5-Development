## Alice Doesn't Live Here Anymore.


The last step in the digital signatures process is for Bob to match the hash values of the message and the signature. 

<br>
<figure class="snippetimg" style="margin: 0 auto;width:90%">
  <img src=".guides/img/Forsalesigns.jpg" alt="https://commons.wikimedia.org/wiki/File% A forest of for sale signs in Oughtibridge UK.By Infrogmation of New Orleans [CC BY 2.0], via Wikimedia Commons">
  <figcaption style="font-size: 0.8em; text-align: left;">  For sale signs in Oughtibridge UK
  </br>
By Terry Robinson [CC BY-SA 2.0] via Wikimedia Commons</figcaption>
</figure>


If Alice’s signature on a message does not match, one of two things might have happened:
1. It wasn’t Alice’s private key that was used to sign the message.

OR

2. The message was altered en route. 

Either way, the integrity of the message is compromised.
