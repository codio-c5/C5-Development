#!/usr/bin/env python
#
import sys, os.path

keyIndex = {}
alphabet = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

encrypt=False
if len(sys.argv) > 1 and sys.argv[1] == 'encrypt':
	encrypt=True

fk="/home/codio/workspace/substitution/subkey.txt"
if os.path.isfile(fk):
    keyfile = open(fk,"r")
    key = keyfile.read()
    keyfile.close
else:
    key = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

fp="/home/codio/workspace/substitution/subplaintext.txt"
if os.path.isfile(fp):
    pfile = open(fp,"r")
    plaintext = pfile.read()
    pfile.close
else:
    plaintext = "Never say never"

def buildKey(key, alphabet):
    tmpkey = []
    missing = []

    keylen = len(key)-1

    # construct key list from key string
    keylen=0
    for k in key:
        if k != '\n':
            tmpkey.append(k)
            keylen+=1

    # fill in missing alphabetic characters if key is incomplete
    i=0
    for a in alphabet:
        if i >= keylen:
            missing += a.upper()
        i+=1

    newkey = tmpkey + missing 

    keyIndex = dict(zip(alphabet, newkey))
    return keyIndex

def subEncrypt(plaintext, keyIndex):
    return ''.join(keyIndex.get(c.lower(), c) for c in plaintext)


def subDecrypt(cipheritext, keyIndex):
    revIndex = dict((v, k) for k, v in keyIndex.iteritems())
    return ''.join(revIndex.get(c, c) for c in ciphertext)

keyIndex = buildKey(key, alphabet)

ciphertext = subEncrypt(plaintext, keyIndex )
newplaintext  = subDecrypt(ciphertext, keyIndex)

if encrypt:
	print(ciphertext)
else:
	print(newplaintext)
