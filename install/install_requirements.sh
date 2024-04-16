#!/usr/bin/env bash

# Install all required libraries t
function installWithPip {
  echo "Install with pip"

  echo "Prepare pip"
  pip install --upgrade pip --no-warn-script-location   
  pip install setuptools --no-warn-script-location
  
  echo "Install requierments with pip"
  pip install --no-cache-dir -r pip/requirements.txt --no-warn-script-location

}

installWithPip
