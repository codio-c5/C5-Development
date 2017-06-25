#!/usr/bin/env python
#
import sys, os.path

keyIndex = {}
alphabet = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newkey = []

encrypt=False
if len(sys.argv) > 1 and sys.argv[1] == 'encrypt':
	encrypt=True

#fk="/home/codio/workspace/substitution/subkey.txt"
fk="/home/paul/work/subkey.txt"
if os.path.isfile(fk):
    keyfile = open(fk,"r")
    key = keyfile.read()
    keyfile.close
else:
    key = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

#fp="/home/codio/workspace/substitution/subplaintext.txt"
fp="/home/paul/work/subplaintext.txt"
if os.path.isfile(fp):
    pfile = open(fp,"r")
    plaintext = pfile.read()
    pfile.close
else:
    plaintext = "Never say never"

def buildKey(key, alphabet):
    tmpkey = []
    tmp = {}

    # construct key
    for a in alphabet:
        tmp[a]=a.upper()

    keyIndex = dict(zip(alphabet, key.rstrip()))
    for a in alphabet:
        if a in keyIndex:
            v=keyIndex[a].lower()
            #print a,":",keyIndex[a]," | ",v,":",tmp[v]
            tmp.pop(v)

    # finish building key if not complete
    i=0
    leftover=tmp.values()
    if len(leftover) > 0:
        for a in alphabet:
            if not keyIndex.has_key(a):
                keyIndex[a]=leftover[i]
                i+=1

    for a in alphabet:
        newkey = ''.join(keyIndex[a])

    if os.path.isfile(fk):
        keyfile = open(fk,"w")
        keyfile.write(''.join(newkey))
        keyfile.close

    return keyIndex

def subEncrypt(plaintext, keyIndex):
    return ''.join(keyIndex.get(c.lower(), c) for c in plaintext)


def subDecrypt(cipheritext, keyIndex):
    revIndex = dict((v, k) for k, v in keyIndex.iteritems())
    return ''.join(revIndex.get(c, c) for c in ciphertext)

keyIndex = buildKey(key, alphabet)
print keyIndex

ciphertext = subEncrypt(plaintext, keyIndex )
newplaintext  = subDecrypt(ciphertext, keyIndex)

if encrypt:
	print(ciphertext)
else:
	print(newplaintext)
