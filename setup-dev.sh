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
pipenv install --dev

cd ../ui

rm -rf node_modules
npm install -D

cd ..
