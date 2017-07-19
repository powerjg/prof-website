set -e # exit if something fails so we don't do anything we shouldn't

git clone git@github.com:powerjg/cvcreator

virtualenv -p /usr/bin/python2.7 venv
. venv/bin/activate

pip install -r cvcreator/requirements.txt
