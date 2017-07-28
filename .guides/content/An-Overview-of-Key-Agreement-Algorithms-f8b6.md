

<div>
  <iframe src="//player.vimeo.com/video/222886876" width="500" height="330" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>

<br>
## Advantages and Disadvantages
The key distribution problem is solved because users share only a public key to create the session key. The session key that they compute is very hard to solve for without knowing one of the private keys or even knowing both the public keys.

After the initial public key exchange used to create the session key, the process mirrors symmetric key encryption, with the session key acting as the shared key that both encrypts and decrypts messages between the users. A session key can be used once or many times.

Like other forms of public key cryptography, key agreement protocols are vulnerable to man-in-the-middle attacks. 

The animation here provides one example of how key agreement protocols work. The approach is different for different protocols. In the next lab, you'll learn about how the Diffie-Helman Key Exchange Protocol works.  Note the differences as well as the similarities with the approach described in the animation.
