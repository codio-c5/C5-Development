#!/bin/bash

if [ -f rsa/encrypted.txt ] ; then
	rm -f rsa/encrypted.txt
	echo "rm encrypted.txt"
fi
if [ -f rsa/private.key ] ; then
	rm -f rsa/private.key
	echo "rm private.key..."
fi
if [ -f rsa/public.key ] ; then
	rm -f rsa/unencrypted.txt
	echo "rm unencrypted.txt"
fi
