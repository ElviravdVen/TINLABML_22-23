#!/usr/bin/env bash

# Install all required libraries t
function installWithPip {
  echo "Install with pip"

  echo "Prepare pip"
  python -m pip install --upgrade pip    
  python -m pip install setuptools
  python -m pip install -U sentence-transformers
  echo "Install requierments with pip"
  python -m pip install --no-cache-dir -r pip/requirements.txt

}

installWithPip
