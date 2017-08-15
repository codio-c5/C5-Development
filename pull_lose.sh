#!/bin/bash
echo "!!!! YOU WILL LOSE ANY LOCAL CHANGES IF YOU PROCEED !!!!"
echo "Are you sure? (yes/no)"
read reply
choice=$(echo $reply|sed 's/(.*)/L1/')
if [ "$choice" = 'yes' ] 
then
  git reset HEAD --hard
  git pull origin master
else
  echo "Aborted. Latest version was NOT pulled."
fi