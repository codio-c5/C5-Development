#!/bin/bash
clear
echo "DO NOT USE double quotes in your commit message. This will not push."
echo "If you want to abort, press ctrl+c."
echo "Enter your commit message now:"
read cmess
git add -A
git commit -am $cmess
