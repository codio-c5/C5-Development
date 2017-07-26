#!/bin/bash

cd rsa
if [ -f encrypted.txt ] ; then
	rm -vf encrypted.txt
fi
if [ -f private.key ] ; then
	rm -vf private.key
fi
if [ -f public.key ] ; then
	rm -vf public.key 
fi
