#!/bin/bash
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    exit
fi
if ! command -v npm &> /dev/null
then
    echo "npm could not be found"
    exit
fi

cd backend
python3 -m pip install --user pipenv
if ! command -v pipenv &> /dev/null
then
    alias pipenv=$(python3 -m site --user-base)/bin/pipenv
fi
pipenv install --dev

cd ../ui

rm -rf node_modules
npm install -D

cd ..
