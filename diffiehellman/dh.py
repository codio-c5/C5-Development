#!/usr/bin/env
#
#
import sys, os

# example :
# Alice & Bob agree on shared/public values P=23, G=5
# Alice chooses her secret number a=6
# Bob chooses his secret number a=6
# They compute G^A mod P => 8; 8 is their encryption key

def usage():
	print """Usage:
	dh.py <modulus P> <base G> <shared number>
	ex: dh.py 23 5 6
	"""
	exit(1)

def main():
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

	os.system('clear') 

	arguments = sys.argv
	if len(arguments) < 4:
		usage()

	arguments = arguments[1:]
	#print "arguments=",arguments
	P = int(sys.argv[1])
	G = int(sys.argv[2])
	S = int(sys.argv[3])

	if P > 97:
		print P,"is > 100"
		print "Please choose a prime number less than 100"
		sys.exit()

	if G > 97:
		print P,"is > 100"
		print "Please choose a prime number less than 100"
		sys.exit()

	if P not in primes:
		print P,"is not a prime"
		print "Please choose a prime number"
		sys.exit()

	if G not in primes:
		print G,"is not a prime"
		print "Please choose a prime number"
		sys.exit()

	#print "P=",P
	#print "G=",G
	#print "S=",S

	# calculate shared value G^S mod P
	mypubkey = G**S % P

	print "Your public key =",mypubkey," please share it with your partner"

	extpubkey = input("Enter your partners public key: ")

	privkey = extpubkey**S % P

	os.system('clear') 
	print "Your shared private key = ",privkey

	f = open('priv.key','w')
	print >> f, privkey

main()
