conda env create -f env.yaml
eval "$(conda shell.bash hook)"
conda activate test
pip install pyttsx3==2.71
BASEDIR=$(readlink -f "$0")
BASEDIR=$(dirname $BASEDIR)
sudo ln -s $BASEDIR/Assistant /usr/local/bin
chmod 777 /usr/local/bin/Assistant
