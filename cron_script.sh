#!/bin/sh

export PATH=/usr/local/bin:$PATH

# This configuration is for my system. You might have to change this for your system to make sure that the slot_checker.py runs on python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh

# This has to be changed to the repository path on your system.
cd <PATH>/cowin-vaccine-slot-checker/
python3 slot_checker.py