#!/bin/sh
#
lab1="lab-part1"
lab2="lab-part2"
lab3="lab-part3"
#
if [ ! -f $lab1/$1 ]; then
	echo "Private key not found"
elif [ ! -f $lab2/$2 ]; then
	echo "Ciphertext not found"
else
	python rsa/rsa.py decrypt $lab1/$1 $lab2/$2 $lab3/$3
fi
