To get started, run the build_nfl_database.sh script that is with the CSV files in the /data folder. This will build the 'nfl' database, and its collection will be named 'play.'

To test that the script correctly, open the Mongo shell and type: 

> show dbs

The output should be:

admin (empty)
local 0.078GB
nfl   0.453GB

Then just type:

> use nfl

to start using the database from the Mongo shell.
