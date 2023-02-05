#!/bin/bash
pipenv run server &
pid1=$!

python -m http.server 8080 &
pid2=$!

sleep 1
open http://localhost:8080/settings.html

trap "kill $pid1 $pid2" EXIT
wait $pid1 $pid2