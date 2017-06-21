


Simple substitution ciphers offer little more security than shift ciphers do. Polygraphic ciphers provide more security by effectively increasing the key size, but ultimately do not provide adequate encryption for modern needs.

You can break simple substitution ciphers like shift ciphers by using pen and paper. The polymorphic version is more difficult but will give away its secrets if you use a cryptanalysis technique called frequency analysis.

In everyday English, you'll see that some letters are used more frequently than others. For instance, the letters "E", "T" and "A" are used much more frequently than "X", "Q" and "Z". 


<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/FreqAnalysis.png" alt="Source: “English letter frequency (alphabetic)” by Nandhp. Public Domain.">
  <figcaption style="font-size: 0.8em; text-align: left;"> English letter frequency (alphabetic) 
  </br>
 Source: by Nandhp. Public Domain.</figcaption>
</figure>




This analysis can be extended to letter groupings like [bigrams](https://en.wikipedia.org/wiki/Bigram) and [trigrams](https://en.wikipedia.org/wiki/Trigram) plus words. It won't be a surprise that words like "the" and "it" occur more frequently than words like "cryptanalyst". 

Knowledge like this helps cryptanalysts break down and ultimately break ciphertext.  More complex ciphers require more time to crack.  Once you have the key to a substitution cipher, it takes less time to decrypt a message compared to what is spent encrypting it.

Encryption ciphers should be very, very one-sided, meaning that the cost of surreptitiously decrypting a message should be much, much, much more expensive than the cost of encrypting it. This requirement drives all of today's encryption methods.