#!bin/bash
    PLAYS="*pbp*.csv"
    PLAYERS="players*.csv"
    WEATHER="weather*.csv"
    COMBINE="combine*.csv"
    for i in $PLAYS
    do
        mongoimport -d nfl -c play --type csv --file "$i" --headerline
    done
    
    for j in $PLAYERS
    do
        mongoimport -d nfl -c player --type csv --file "$j" --headerline
    done

    for k in $WEATHER
    do
        mongoimport -d nfl -c weather --type csv --file "$k" --headerline
    done

    for l in $COMBINE
    do
        mongoimport -d nfl -c combine --type csv --file "$l" --headerline
    done
