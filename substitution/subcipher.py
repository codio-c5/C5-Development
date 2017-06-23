#!/usr/bin/env python
#
import sys

encrypt=False
if sys.argv[1] == 'encrypt':
	encrypt=True

keyfile = open("/home/codio/workspace/substitution/subkey.txt","r")
key = keyfile.read()
keyfile.close

alphabet = 'abcdefghijklmnopqrstuvwxyz'
#key = 'ZYXWVUTSRQPONMLKJIHGFEDCBA '

keyfile = open("/home/codio/workspace/substitution/subplaintext.txt","r")
plaintext = keyfile.read()
keyfile.close
#plaintext = "What are you talking about? What's this about?"

def subEncrypt(plaintext, key, alphabet):
    keyIndex = dict(zip(alphabet, key))
    return ''.join(keyIndex.get(c.lower(), c) for c in plaintext)

def subDecrypt(cipheritext, key, alphabet):
    keyIndex = dict(zip(key, alphabet))
    return ''.join(keyIndex.get(c, c) for c in ciphertext)

ciphertext = subEncrypt(plaintext, key, alphabet)
newplaintext  = subDecrypt(ciphertext, key, alphabet)

if encrypt:
	print(ciphertext)
else:
	print(newplaintext)
