#!/usr/bin/env bash

# Install all required libraries t
function installWithPip {
  echo "Install with pip"

  echo "Prepare pip"
  pip install --upgrade pip    
  pip install setuptools
  pip install -U sentence-transformers
  echo "Install requierments with pip"
  pip install --no-cache-dir -r pip/requirements.txt

}

installWithPip
