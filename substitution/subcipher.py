#!/usr/bin/env python
#
import sys, os.path

alphabet = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#defkey =   'zyxwvutsrqponmlkjihgfedcba'
defkey = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
defplaintext = "Never say never"
fp="/home/codio/workspace/substitution/subplaintext.txt"
fc="/home/codio/workspace/substitution/subciphertext.txt"
fk="/home/codio/workspace/substitution/subkey.txt"
keyIndex = {}
newkey = []
action=0

#if len(sys.argv) > 1 and sys.argv[1] == 'encrypt':
if sys.argv[1] == 'init':
	action=0
elif sys.argv[1] == 'encrypt':
	action=1
else:
	action=2


def buildKey(key, alphabet):
    tmpkey = []
    tmp = {}

    # construct alphet
    for a in alphabet:
        tmp[a]=a.upper()

    keyIndex = dict(zip(alphabet, key.rstrip()))
    for a in alphabet:
        if a in keyIndex:
            v=keyIndex[a].lower()
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

#    if os.path.isfile(fk):
#        keyfile = open(fk,"w")
#        keyfile.write(''.join(newkey))
#        keyfile.close

    return keyIndex

def init():
	keyfile = open(fk,"w")
	keyfile.write(defkey)
	keyfile.close
	pfile = open(fp,"w")
	pfile.write(defplaintext)
	pfile.close

def subEncrypt():
	keyfile = open(fk,"r")
	key = keyfile.read()
	keyfile.close
	pfile = open(fp,"r")
	plaintext = pfile.read()
	pfile.close
	keyIndex=buildKey(key, alphabet)
	return ''.join(keyIndex.get(c.lower(), c) for c in plaintext)


def subDecrypt(ciphertext):
	keyfile = open(fk,"r")
	key = keyfile.read()
	keyfile.close
	keyIndex=buildKey(key, alphabet)
	revIndex = dict((v, k) for k, v in keyIndex.iteritems())
	return ''.join(revIndex.get(c, c) for c in ciphertext)


# init
if action==0:
	init()
# Encrypt
elif action==1:
	print(subEncrypt())
# Decrypt
else:
	ciphertext = subEncrypt()
	print (subDecrypt(ciphertext))
