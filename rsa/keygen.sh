#!/bin/sh

python rsa/rsa.py keys $1 $2
mv private.key lab-part1
mv public.key  lab-part1
