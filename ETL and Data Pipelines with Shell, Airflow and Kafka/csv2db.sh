# This script
# Extracts data from /etc/passwd file into a CSV file.

# The csv data file contains the user name, user id and
# home directory of each user account defined in /etc/passwd

# Transforms the text delimiter from ":" to ",".
# Loads the data from the CSV file into a table in PostgreSQL database.

# Extract phase
echo "Extracting data"

# column 1, 3, 6 are columns

cut -d ":" -f1,3,6 /etc/passwd > extracted-data.txt

# Transform phase
echo "Transforming data"
tr ":" "," < extracted-data.txt > transformed-data.csv

# Loading phase
echo "Loading data"

export PGPASSWORD=LQsjUoaTnDuPjwB5G8cycXKq

echo "\c template1;\COPY users FROM '/home/project/transformed-data.csv' DELIMITERS ',' CSV;" | psql --username=postgres --host=postgres

echo "Data loaded successfully"