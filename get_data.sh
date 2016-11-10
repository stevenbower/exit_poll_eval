#!/usr/bin/env bash

mkdir -p ./input

for y in 2008 2012 2016; do
  for s in $(cat states.txt); do 
    echo "Fetching: ${y}-${s}"
    curl http://data.cnn.com/ELECTION/${y}/${s}/xpoll/Pfull.json > ./input/${y}-${s}.json
  done
done

# clean up empty files
find ./input -type f -size 0 -name "*.json" -exec rm {} \;
