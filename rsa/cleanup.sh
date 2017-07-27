#!/bin/bash
#
echo $1
lab=$1
lab1="lab-part1"
lab2="lab-part2"

if [ $lab = "lab-part1" ]; then
	if [ -f $lab1/private.key ] ; then
		rm -vf $lab1/private.key
	fi
	if [ -f $lab1/public.key ] ; then
		rm -vf $lab1/public.key 
	fi
elif [ "$lab" = "lab-part2" ]; then
	if [ -f $lab2/public.key ] ; then
		rm -vf $lab2/public.key
	fi
	if [ -f $lab2/cipher.txt ] ; then
		rm -vf $lab2/cipher.txt
	fi
else
	if [ -f $lab3/cipher.txt ] ; then
		rm -vf $lab3/cipher.txt
	fi
fi
