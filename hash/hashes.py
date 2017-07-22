#!/usr/bin/env
#
import sys, os, hashlib

# example :
# 

def usage():
        print """Usage:
        hashes.py string
        ex: dh.py hello world
        """
        exit(1)

def main():
#        os.system('clear')

        arguments = sys.argv
        if len(arguments) < 2:
                usage()

        s = arguments[1]
        print "string =",s

	hash_object = hashlib.md5(s.encode())
	h=(hash_object.hexdigest())
	print "MD5:	",h

	hash_object = hashlib.sha1(s.encode())
	h=(hash_object.hexdigest())
	print "SHA1:	",h

	hash_object = hashlib.sha256(s.encode())
	h=(hash_object.hexdigest())
	print "SHA256:	",h

	hash_object = hashlib.sha512(s.encode())
	h=(hash_object.hexdigest())
	print "SHA512:	",h

main()
