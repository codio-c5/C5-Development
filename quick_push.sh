#!/bin/bash
echo "This assumes you have just committed your changes. Do you want to PUSH to the remote repo? (yes/no)"
read reply
choice=$(echo $reply|sed 's/(.*)/L1/')
if [ "$choice" = 'yes' ] 
then
  echo "git push origin master"
  git push origin master
else
  echo "Aborted. Latest version was NOT pushed."
fi