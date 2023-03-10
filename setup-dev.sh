#!/bin/bash
cd backend
# ensure python is version 3
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    cd ..
    exit
fi
python3 -m pip install --user pipenv
if ! command -v pipenv &> /dev/null
then
    alias pipenv=$(python3 -m site --user-base)/bin/pipenv
fi
# install dependencies
pipenv install --dev

cd ../ui
# ensure npm is installed
if ! command -v npm &> /dev/null
then
    echo "npm could not be found"
    cd ..
    exit
fi
rm -rf node_modules
# install dependencies
npm install -D
cd ..
