## Linking Your Roots 

CAs use the trusted root certificate to create a **chain of trust,** or **certificate path** in which all of the certificates signed by the root certificate inherit the trustworthiness of the root certificate.  

  <figure class="snippetimg" style="margin: 0 auto;width:110%">
  <img src=".guides/img/Chainoftrust.svg" alt="https://commons.wikimedia.org/wiki/File:Chain_of_trust.svg">
  <figcaption style="font-size: 0.8em; text-align: left;">  Chain of trust. <br>
By Yanpas (Own work) [CC BY-SA 4.0], via Wikimedia Commons.
</figure>
<br>

Here's how it works. At the the top of the chain is the **end-entity certificate,** and at the bottom of the chain is the **root certificate.** between them may be any number of **intermediate CA certificates.**

Starting with end-entity certificate, each certificate is signed by the next certificate in the chain. The intermediate CA certificate is signed by the root CA certificate.  CAs often have one or more intermediate CA certificates that they also control. It allows them to keep tighter security restrictions on their root CA certificate, protecting it from compromise.


