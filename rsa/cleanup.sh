#!/bin/bash
#
if [ -d lab-part1 ]; then
	rm -vf lab-part1/*
fi
if [ -d lab-part2 ]; then
	rm -vf lab-part2/*
	echo "" > lab-part2/message.txt
fi
if [ -d lab-part3 ]; then
	rm -vf lab-part3/*
	echo "" > lab-part3/partner-message.txt
fi
