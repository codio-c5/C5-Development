#!/bin/sh

if [ -f $1 ]; then
	python rsa/rsa.py decrypt $1 $2 $3
else
	echo "Private key not found"
fi
