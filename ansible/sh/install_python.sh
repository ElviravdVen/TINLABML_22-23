#!/usr/bin/env bash

echo "Install software-properties-common"
sudo apt install software-properties-common 

echo "Reinstall ca-certificates"
sudo apt-get install --reinstall ca-certificates 

echo "Add ppa"
sudo add-apt-repository 'deb https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy main'

echo "Update"
sudo apt update 

echo "Install python 3.10"
sudo apt install python3.10 

echo "Install pip"
sudo apt install python3-pip 

echo "Make python 3.10 default"
sudo ln -s /usr/bin/python3.10 /usr/bin/python
