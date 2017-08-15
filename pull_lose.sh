#!/bin/bash
echo "!!!! ANY CHANGES YOU HAVE MADE WILL BE LOST !!!"
read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    git reset HEAD --hard
    git pull origin master
elif
  echo "Aborted. Latest version was NOT pulled."
fi