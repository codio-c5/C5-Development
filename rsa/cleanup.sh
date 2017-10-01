#!/bin/bash
#
cd ~/workspace
#
if [ -d lab-part1 ]; then
	rm -vf lab-part1/*
else
	mkdir lab-part1
fi
if [ -d lab-part2 ]; then
	rm -vf lab-part2/*
	echo "" > lab-part2/message.txt
	echo "" > lab-part2/message.txt
else
	mkdir lab-part2
fi
if [ -d lab-part3 ]; then
	rm -vf lab-part3/*
	echo "" > lab-part3/partner-message.txt
else
	mkdir lab-part3
	echo "" > lab-part3/partner-message.txt
fi
