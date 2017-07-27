#!/bin/sh
#
if [ -f lab-part2/partner-pubkey.txt ] ; then
	pubkeyname=`cat lab-part2/partner-pubkey.txt`
else
	pubkeyname=public.key
fi
#
if [ -f lab-part2/$pubkeyname ] ; then
	python rsa/rsa.py encrypt lab-part2/$pubkeyname $2 $3
else
	echo "Please upload your partner's public key to lab-part2"
fi
