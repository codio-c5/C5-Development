
## Down to the Roots
||| definition
A **certificate authority (CA)** is a trusted third party that issues digital certificates. These certificates verify the owner of a public key, which authenticates the owner's identity on the internet.
|||

A CA signs these certificates using its private key. Its public key is published in a self-signed CA certificate, called a **trusted root certificate.** 



CAs use the trusted root certificate to create a **chain of trust,** in which all of the certificates signed by the root certificate inherit the trustworthiness of the root certificate.  Many root certificates are embedded in web browsers so they have built-in trust of those CAs. 
Web servers, email clients, smartphones, and many other types of hardware and software also support PKI and contain trusted root certificates from the major CAs.
