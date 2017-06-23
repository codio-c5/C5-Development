#!/usr/bin/env python
#
import sys

encrypt=False
if sys.argv[1] == 'encrypt':
	encrypt=True


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'ZYXWVUTSRQPONMLKJIHGFEDCBA '
#plaintext = "Never say never"
plaintext = "What are you talking about? What's this about?"

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
