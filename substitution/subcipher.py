#
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'ZYXWVUTSRQPONMLKJIHGFEDCBA '
#plaintext = "Never say never"
plaintext = "What are you talking about? What's this about?"

def encrypt(plaintext, key, alphabet):
    keyIndex = dict(zip(alphabet, key))
    return ''.join(keyIndex.get(c.lower(), c) for c in plaintext)

def decrypt(cipheritext, key, alphabet):
    keyIndex = dict(zip(key, alphabet))
    return ''.join(keyIndex.get(c, c) for c in ciphertext)

ciphertext = encrypt(plaintext, key, alphabet)
newplaintext  = decrypt(ciphertext, key, alphabet)

print(ciphertext)
print(newplaintext)


On Thu, Jun 22, 2017 at 9:49 PM, paul <pgsery@gmail.com> wrote:

    #
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 'ZYXWVUTSRQPONMLKJIHGFEDCBA '
    plaintext = "Never say never"

    def encrypt(plaintext, key, alphabet):
        keyIndex = dict(zip(alphabet, key))
        return ''.join(keyIndex.get(c.lower(), c) for c in plaintext)

    def decrypt(cipheritext, key, alphabet):
        keyIndex = dict(zip(key, alphabet))
        x=''
        for c in ciphertext:
            if c is None:
                    print "none:",c
                    next
            else:
                    x += keyIndex.get(c)
        print x

    ciphertext = encrypt(plaintext, key, alphabet)
    plaintext  = decrypt(ciphertext, key, alphabet)

    print(ciphertext)
