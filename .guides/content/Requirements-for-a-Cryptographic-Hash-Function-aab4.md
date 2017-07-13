### Not all hash functions are created equal.  Non-cryptographic hash functions do not live up to the stringent requirements that cryptographic hash functions must meet. 

These requirements are: 

- **Fixed size hash value.** No matter what the size of the original data, the output, or **hash value,** is always a fixed number of bits.

- **Pre-image resistant.** It is nearly impossible to factor the original data for a given hash value.  A hash function is a one-way process that cannot be reversed to find the input value.


<br>
<figure class="snippetimg" style="margin: 0 auto;width:70%">

  <img src=".guides/img/SnowflakesWilsonBentley.jpg" alt="Public key cryptography inventors Whitfield Diffie and Martin Hellman. . *Source: Whitfield Diffie photo by Mary Holzer licensed under CC-BY and Martin Hellman originated from Martin Hellman licensed under GFDL.*
">
  <figcaption style="font-size: 0.8em; text-align: left;">Snowflakes. 
</br>
 By Wilson Bentley [Public domain], via Wikimedia Commons</figcaption>
</figure>

- **Collision resistant.** Hash values are like snowflakes. It is computationally infeasible  to find two inputs that have the same hash value. Infeasible, but theoreticahlly, still possible.  Since hash functions map long input values to a shorter compressed value, it is theoretically possible for sequences of bits to map to the same hash value. A **collision** occurs when two messages that have the same hash value.

- **Efficient.** Hash values are fast and easy to compute.  This makes them practical for storage and for use on even small devices.


<br>
<figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/Roulette.jpg" alt="Public key cryptography inventors Whitfield Diffie and Martin Hellman. . *Source: Whitfield Diffie photo by Mary Holzer licensed under CC-BY and Martin Hellman originated from Martin Hellman licensed under GFDL.*
">
  <figcaption style="font-size: 0.8em; text-align: left;">A roulette wheel. 
</br>
 By Conor Ogle from London, UK (Spin) [CC BY 2.0 (http://creativecommons.org/licenses/by/2.0)], via Wikimedia Commons</figcaption>
</figure>


- **Pseudorandomness:** The hash values pass tests designed to detect pseudorandomness. Generating truly random numbers is actually quite difficult, even with a computer. Typically, numbers generated from an algorithm are following a set of instructions that are not truly random. Data sets used have ranged from solar radiation to keystroke patterns, all in pursuit of the truly random.  A pseudorandomness test verifies that the hash value meets a minimum bar for statistical randomness. 


