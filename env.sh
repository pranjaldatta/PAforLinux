#!/bin/bash

#create conda env
conda env create -f env.yaml
eval "$(conda shell.bash hook)"
conda activate LinuxPA

#create symlink at /usr/local/bin of Assistant
BASEDIR=$(readlink -f "$0")
BASEDIR=$(dirname $BASEDIR)
sudo ln -s $BASEDIR/Assistant /usr/local/bin
chmod 777 /usr/local/bin/Assistant

#get chromedriver
RES="$(google-chrome --version)"
RES="$(echo $RES | cut -d' ' -f3)"
A="$(echo $RES | cut -d'.' -f1)"
if [[ $A == "79" ]];
then
    echo "Getting chrome driver for version 79 ..."
    sudo wget -P /usr/local/bin/ https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip
    sudo unzip /usr/local/bin/chromedriver_linux64.zip -d /usr/local/bin
fi
if [[ $A == "80" ]]
then 
    echo "Getting chrome driver for version 80 ..."
    sudo wget -P /usr/local/bin https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_linux64.zip
    sudo unzip /usr/local/bin/chromedriver_linux64.zip -d /usr/local/bin
fi   

#install espeak
sudo apt-get install espeak

#installing extra dependencies
pip install pyttsx3==2.71
sudo src/modules/notes/install.sh i


