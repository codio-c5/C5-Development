To build the chain of trust, public key infrastructure has five primary components.  It starts with the certificate authority.

1. **A certificate authority (CA)** , is a trusted party that acts as the root of trust and provides services that authenticate the identity of individuals, computers, web sites, and other digital entities.
1. **Root Certificate Authority certificate (root CA certificate)**, is root-trusted party which is represented by a self signed certificate.

 <figure class="snippetimg" style="margin: 0 auto;width:80%">
  <img src=".guides/img/Elements.jpg" alt="https://commons.wikimedia.org/wiki/File:Chain_of_trust.svg">
  <figcaption style="font-size: 0.8em; text-align: left;">  Of Winds and Four Seasons. A meteorological and astronomical diagram. <br>
By Johannes Regiomontanus, 1512. Woodcut on paper. [Public domain], via Wikimedia Commons.
</figure>
<br>

3. **A registration authority (RA).** Usually subordinate to the CA, the RA validates certificate signing requests for CAs, and authenticates user identities.  The registration authority authorizes the CA to issue the certificate. 

1. **A certificate database,** which stores certificate requests and issues and revokes certificates.

1. **A certificate store,** which resides on a local computer as a place to store issued certificates, private keys, and  certificate requests.
