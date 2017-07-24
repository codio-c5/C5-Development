
## The Roots of Trust
|||definition
A **certificate authority (CA)** is a trusted entity that issues digital certificates.  Certificates typically include the owner's name and public key, the validity period of the certificate, the algorithm used, and the digital signature. A certificate authority signs certificates using its private key. Its public key is published in a self-signed CA certificate, called a **trusted root certificate.** 
|||

<br>
  <figure class="snippetimg" style="margin: 0 auto;width:100%">
  <img src=".guides/img/PreahKhan.jpg" alt="https://commons.wikimedia.org/wiki/File:NYS-Notary-Seal.jpg">
  <figcaption style="font-size: 0.8em; text-align: left;">  Tree roots penetrating a temple at Preah Kahn. <br>
By Anne Hamilton. Used with permission of the photographer.
</figure>
<br>

CA's provide services that authenticate the identity of individuals, computers and other entities. Many root certificates are embedded in web browsers so they have built-in trust of those CAs. Web servers, email clients, smartphones, and many other types of hardware and software use PKI and contain trusted root certificates from  major CAs.
