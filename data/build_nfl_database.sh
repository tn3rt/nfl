#!bin/bash
    FILES="*.csv"
    for f in $FILES
    do
        mongoimport -d nfl -c play --type csv --file "$f" --headerline
    done
