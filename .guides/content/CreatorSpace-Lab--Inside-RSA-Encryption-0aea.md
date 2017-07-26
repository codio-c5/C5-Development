

In this lab you will use RSA to encrypt and decrypt a file from the Linux command line. You will generate a key pair and encrypt and decrypt messages using RSA.

Start by clean everything up in your folder. Click the clean up button.

{Clean Up}(sh rsa/cleanup.sh)

## Generate a Key Pair
First you will generate a key pair. A key pair consists of a private key and a public key.

{Generate keys}(sh rsa/keygen.sh) 

This runs the command ```python rsa/rsa.py keys```

You can view the contents of the private ```private.key``` key and public ```public.key``` key by clicking them in the tree on the left.

## Encrypt a File

Assume that you are Alice. Bob will have sent you his public key so that you are able to decrypt messages the that he sends you. 

Imagine that you have a plaintext file that is ready to sent. You can encrypt the file to send to Bob using Bob's public key. 

{Encrypt a file}(sh rsa/encrypt.sh encrypt public.key plaintext.txt encrypted.txt)

This runs the command ```python rsa/rsa.py encrypt public.key plaintext.txt encrypted.txt``` and puts the ciphertext into the **encrypted.txt** file.

## Decrypt a File

Bob has sent you a ciphertext you want to decrypt. You will have sent Bob your public key beforehand and he would have encrypted his message using your public key.

{Decrypt a file}(sh rsa/decrypt.sh decrypt private.key encrypted.txt plaintext.txt)

1. Decrypt the ciphertext using your private key by entering:
```python rsa.py decrypt private.key encrypted.txt unencrypted.txt```
2. Review Bob's decrypted message to you.

## Hackathon: Under the Hood
This lab was written in Python. Do you want to see what the code looks like? 
1. Open up rsa.py by running the command ```more rsa.py```
2. Use the space bar to show page through the script.

## Check Your Knowledge
{Check It!|assessment}(multiple-choice-1750723723)
{Check It!|assessment}(multiple-choice-3023733973)



## Growth Hack
{Submit Answer!|assessment}(free-text-1268726708)
