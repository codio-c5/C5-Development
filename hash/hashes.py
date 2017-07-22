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
        os.system('clear')

        arguments = sys.argv
        if len(arguments) < 2:
                usage()

        s = arguments[1]
        print "string =",s

	hash_object = hashlib.md5(b's')
	print(hash_object.hexdigest())

main()
