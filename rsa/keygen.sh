#!/bin/sh

python rsa/rsa.py keys $1
#
if [ "$1" = "alice" ]; then
	mv private.key lab-part1/alice-private.key
	mv public.key  lab-part1/alice-public.key
else
	mv private.key lab-part1/bob-private.key
	mv public.key  lab-part1/bob-public.key
fi
