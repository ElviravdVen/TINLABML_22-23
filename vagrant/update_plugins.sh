#!/usr/bin/env bash

echo "Update Plugins"
vagrant plugin update

echo "Install Vagrant VBGuest"
vagrant plugin install vagrant-vbguest

echo "Install Vagrant SCP"
vagrant plugin install vagrant-scp