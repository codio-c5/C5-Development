Simple substitution ciphers offer little more security than shift ciphers do. Polygraphic ciphers provide more security by effectively increasing the key size but ultimately do not provide adaquate encryption.

You can break simple substitution ciphers like shift ciphers by using pen and paper. The polymorphic version is more difficult but will give away its secrets if you use a Crytpanalysis technique called frequency analysis.

If you look at how everyday english is written, you'll see that some letters are used more frequently than others. For instance, the letters "E", "T" and "A" are used much more frequently than "X", "Q" and "Z". 

This analysis can be extened to letter groupings like [bigrams](https://en.wikipedia.org/wiki/Bigram) and [trigrams](https://en.wikipedia.org/wiki/Trigram) plus words. It should not be a surprise that words like "the" and "it" occur more frequently than words like "cryptanalyst" 

Knowledge like this helps the Cryptanylst break down cipher text that helps ultimately break cipher text.  Let's start by borrowing the cipher text from the previous lesson.

WDNH PH RXW WR WKH EDOO JDPH
WDNH PH RXW ZLWK WKH FURZG
EXB PH VRPH SHDQXWV DQG FUDFNHUMDFNV
L GRQ'W FDUH LI L QHYHU JHW EDFN
OHW PH URRW

Click the Frequency analysis button to see the higher occuring letters.

{Frequency analysis}(.guides/getfreq.sh)

Click to see the bigrams.

{Frequency analysis bigrams}(.guides/getbigram.sh)

And trigrams.

{Frequency analysis bigrams}(.guides/gettrigram.sh)

The Cryptanlyst can use this information to 
... This means that there is no cost penalty when trying to decrypt a message compared to what is spent encrypting it. Encryption ciphers should be very, very one-sided, meaning that the cost of surrupticiously decrypting a message should be much, much, much more expensive than the cost of encrypting. That requirement is what drives all of today's encryption methods.