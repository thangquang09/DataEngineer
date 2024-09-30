[Setup and Practice Assignment](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvRmluYWwlMjBBc3NpZ25tZW50L1NldHVwJTIwYW5kJTIwUHJhY3RpY2UlMjBBc3NpZ25tZW50Lm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNTI3MzgwOX0.TyQQOIvXcgJI02zr_RNhC3L_d17vwFNXn8Z5GhcG2Vs)

[Set up cloudant URL](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvQ2xvdWRhbnQvTGFiJTIwLSUyMFVzaW5nJTIwSFRUUCUyMEFQSSUyMHRvJTIwY3JlYXRlJTIwYW5kJTIwcXVlcnklMjBDbG91ZGFudCUyMGRhdGFiYXNlcy9MYWIlMjAtJTIwVXNpbmclMjBIVFRQJTIwQVBJJTIwdG8lMjBjcmVhdGUlMjBhbmQlMjBxdWVyeSUyMENsb3VkYW50JTIwZGF0YWJhc2VzLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcxODk4NDgzNH0.f9vSarMK3-8e4NXroEdVtA3eHKYf0hd8OKPZPGywqkM)

**Set up and Practice Code**

```sh
sudo npm install -g couchimport@1.4.0

couchimport --version

wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
tar -xf mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
export PATH=$PATH:~/project/mongodb-database-tools-ubuntu1804-x86_64-100.3.1/bin
echo "done"

mongoimport --version

export CLOUDANTURL="https://apikey-v2-2aqf0g2ftiqqrmlf2s7uchxiuhbje5i3lb99o0gpg6a1:c47d25882600dc3dd2c35c8281bcae9b@854eb3d0-e70d-43ba-b9f3-536aeb3e4590-bluemix.cloudantnosqldb.appdomain.cloud"

couchexport --url $CLOUDANTURL --db diamonds --delimiter ","

couchexport --url $CLOUDANTURL --db diamonds --type jsonl

couchexport --url $CLOUDANTURL --db diamonds --type jsonl > diamonds.json

couchexport --url $CLOUDANTURL --db diamonds --delimiter "," > diamonds.csv

# start mongo

mongoimport -u root -p MzA2NDAtcnNhbm5h --authenticationDatabase admin --db training --collection diamonds --file diamonds.json --host localhost

mongoexport -u root -p MzA2NDAtcnNhbm5h --authenticationDatabase admin --db training --collection diamonds --out mongodb_exported_data.json --host localhost

mongoexport -u root -p MzA2NDAtcnNhbm5h --authenticationDatabase admin --db training --collection diamonds --out mongodb_exported_data.csv --type=csv --fields _id,clarity,cut,price --host localhost

# start cassandra

# create keyspace training
## create table diamonds with

# id - primary key (use ‘id’ as the primary key(type-varchar); Cassandra does not allow you to create a column starting with underscore(_))
# clarity - text
# cut - text
# price - integer.g

use training;
COPY training.diamonds(id,clarity,cut,price) FROM 'mongodb_exported_data.csv' WITH DELIMITER=',' AND HEADER=TRUE;

COPY diamonds TO 'cassandra-diamonds.csv';
```


[FINAL PROJECT OVERVIEW](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTVNraWxsc05ldHdvcmstREIwMTUxRU4tZWRYL2xhYnMvRmluYWxQcm9qZWN0LzAxLU92ZXJ2aWV3Lm1kIiwidG9vbF90eXBlIjoiaW5zdHJ1Y3Rpb25hbC1sYWIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcxMTYzODY0OH0.-TUZVth_Fa2KGncBqY7p5V92bYDk1dZpLs2czZQTJRY)

[FINAL PROJECT HOW TO SUBMIT](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0RwdV9NM2hobEFkOUxSZnBVU1pqTVEvMDItSW5zdHJ1Y3Rpb25zTmV3LXYxLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNzI1MjA5Mn0.lEQr7HiBsJstOggsKlnVTazSwlhCtj3o9bAkW5a0-8E)