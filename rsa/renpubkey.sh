#!/usr/bin/bash
#
if [ -f lab-part2/partner-pubkey.txt ] ; then
	newname=$(cat lab-part2/partner-pubkey.txt)
	echo $newname
	mv -v lab-part2/$newname lab-part2/x
fi
