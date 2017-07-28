## Using Frequency Analysis 

Simple substitution ciphers offer little more security than shift ciphers do. Recall that **monographic ciphers** replace letters in plaintext one for one with ciphertext. There are also **polygraphic ciphers** that replace multiple letters at a time.  They provide more security by increasing the **key size**, but ultimately they do not provide adequate encryption for modern needs because they are still much too easy to break.

In fact, you can break substitution ciphers, just like shift ciphers, by using pen and paper. The polygraphic version is more difficult, but it will eventually reveal its secrets if you use a cryptanalysis technique called **frequency analysis.**

In everyday English, you'll see that some letters are used more frequently than others. For instance, the letters E, T, and A are used much more frequently than X, Q, and Z.  Letter frequency patterns for English are shown in the graph below.
 <br>

<figure class="snippetimg" style="margin: 0 auto;width:70%">
  <img src=".guides/img/FreqAnalysis.png" alt="Source: “English letter frequency (alphabetic)” by Nandhp. Public Domain.">
  <figcaption style="font-size: 0.8em; text-align: left;"> English letter frequency (alphabetic). 
  </br>
 Source: by Nandhp. Public Domain.</figcaption>
</figure>


This analysis can be extended to letter groupings like [**digrams** (also known as bigrams)](https://en.wikipedia.org/wiki/Bigram) and [**trigrams**](https://en.wikipedia.org/wiki/Trigram), plus common words. It won't be a surprise to you that words like "the" and "it" occur more frequently than words like "cryptanalyst." 

Knowledge like this helps cryptanalysts analyze and ultimately break ciphertext. More complex ciphers require more time to crack, of course. Once you have the key to a substitution cipher, it takes less time to decrypt a message compared to encrypting it.

Encryption ciphers should be very one-sided, meaning that the effort required to surreptitiously decrypt a message should be much, much more expensive and time consuming than the effort to encrypt it. This requirement drives all of today's encryption methods.