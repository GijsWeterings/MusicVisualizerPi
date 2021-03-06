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
# apt-get install -y python-tk

# Update pip to latest version
pip install --upgrade pip

pip install midiutil
pip install pygame


apt-get install timidity
apt-get install libasound2-dev
apt-get install mpg123



apt-get install timidity


git clone git@github.com:zvineyard/light-organ.git ~/light-organ