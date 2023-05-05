#!/bin/bash
if ! command -v pipenv &> /dev/null
then
    alias pipenv=$(python3 -m site --user-base)/bin/pipenv
fi
cd backend
LOG_LEVEL=info pipenv run server &
pid1=$!

cd ../ui
npm run dev &
pid2=$!
cd ..
sleep 2

if ! [ -f /.dockerenv ]; then
    echo "I'm inside matrix ;(";
    if [ "$(uname)" == "Darwin" ]; then
       open http://localhost:8080/
    else
       xdg-open http://localhost:8080/
    fi
fi

trap "kill $pid1 $pid2" EXIT
wait $pid1 $pid2
