#!/usr/bin/env bash

sudo apt update && sudo apt upgrade -y

echo "Update apt"
echo | sudo apt install software-properties-common -y

echo "Add ppa"
echo | sudo add-apt-repository ppa:deadsnakes/ppa

echo "Install python 3.10"
sudo apt install python3.10

echo "Install pip"
sudo apt install python3-pip -y
