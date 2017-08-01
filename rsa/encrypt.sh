#!/bin/sh
#
lab2="lab-part2"
#
if [ -f $lab2/$1 ] ; then
	python rsa/rsa.py encrypt $lab2/$1 $lab2/$2 $lab2/$3
else
	echo "Please upload your partner's public key to lab-part2"
fi
