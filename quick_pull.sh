#!/bin/bash
echo "This assumes you have just committed your changes. Do you want to pull from the remote repo? (yes/no)"
read reply
choice=$(echo $reply|sed 's/(.*)/L1/')
if [ "$choice" = 'yes' ] 
then
  git pull origin master
else
  echo "Aborted. Latest version was NOT pulled."
fi