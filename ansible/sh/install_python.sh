#!/usr/bin/env bash

# https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa

echo "Install software-properties-common"
sudo apt install software-properties-common 

echo "Reinstall ca-certificates"
sudo apt-get install --reinstall ca-certificates 

# TODO
# https://stackoverflow.com/questions/68992799/warning-apt-key-is-deprecated-manage-keyring-files-in-trusted-gpg-d-instead

echo "Sign"
sudo apt-key adv --keyserver "hkp://keyserver.ubuntu.com:80" --recv "F23C5A6CF475977595C89F51BA6932366A755776"

echo "Add ppa"
sudo add-apt-repository "deb https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu focal main "
sudo add-apt-repository "deb-src https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu focal main "

echo "Update"
sudo apt update 

echo "Install python 3.10"
sudo apt install python3.10 

echo "Install pip"
sudo apt install python3-pip 

echo "Make python 3.10 default"
sudo ln -s /usr/bin/python3.10 /usr/bin/python
