#!/usr/bin/env bash

echo | sudo apt-add-repository ppa:ansible/ansible 
sudo apt -y update
sudo apt install -y ansible
sudo apt install -y cowsay

pip install --upgrade pip ansible-core==2.12.7