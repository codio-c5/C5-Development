import random

alpha = "abcdefghijklmnopqrstuvwxyz"
key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
plaintext = "Never say Never"

def encrypt(plaintext, key, alphab):
    d = dict(alphabet, key)
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

#def decrypt(cipher, key, alphabet):
 #   keyMap = dict(zip(key, alphabet))
  #  return ''.join(keyMap.get(c.lower(), c) for c in cipher)

cipher = encrypt(plaintext, key, alpha)

print "plaintext: ",plaintext
print "ciphertext",ciphertext
#print(decrypt(cipher, key, alphabet))
