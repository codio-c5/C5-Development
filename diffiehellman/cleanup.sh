#!/bin/bash
#
HDIR="/home/codio/workspace"
LAB1="dhlab-part1"
LAB2="dhlab-part2"
#
cd $HDIR
if [ ! -d $LAB1 ]; then
	mkdir $LAB1
	res=$?
else
	res=0
fi
if [ $res -eq 0 ]; then
	cd $LAB1
	rm -f *
	ln -s $HDIR/diffiehellman/dh.py
else
	echo "Error, $LAB1 does not exist"
fi
#
cd $HDIR
if [ ! -d $LAB2 ]; then
	mkdir $LAB2
	res=$?
else
	res=0
fi
if [ $res -eq 0 ]; then
	cd $LAB2
	rm -f *
	ln -s $HDIR/aes/aes.py
	echo "I am not a number!" > message.txt
	touch orig-message.txt
else
	echo "Error, $LAB2 does not exist"
fi
