#!/bin/bash
if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "You need to run this as root! run: sudo ./setup.sh"
    exit
fi

# Make sure repository is up to date
apt-get update

apt-get install -y python
apt-get install -y python3
apt-get install -y python-pip
apt-get install -y python-gpiozero
apt-get install -y python3-gpiozero

# Update pip to latest version
pip install --upgrade pip