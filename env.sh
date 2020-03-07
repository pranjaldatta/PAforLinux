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

#installing extra dependencies
pip install pyttsx3==2.71
sudo /src/modules/notes/install.sh i


