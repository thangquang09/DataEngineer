# cp-access-log.sh
# This script downloads the file 'web-server-access-log.txt.gz'
# from "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/".

# The script then extracts the .txt file using gunzip.

# The .txt file contains the timestamp, latitude, longitude 
# and visitor id apart from other data.

# Transforms the text delimeter from "#" to "," and saves to a csv file.
# Loads the data from the CSV file into the table 'access_log' in PostgreSQL database.

# Extract phase

echo "Extracting data"

cut -d"#" -f1-4  /home/project/web-server-access-log.txt > extracted_data.txt

# Transform phase

echo "Transforming data"

tr "#" "," < extracted_data.txt > transformed_data.csv

# Loading phase``

echo "Loading data"

export PGPASSWORD=LQsjUoaTnDuPjwB5G8cycXKq

echo "\c template1;\COPY access_log FROM '/home/project/transformed_data.csv' DELIMITERS ',' CSV HEADER;" | psql --username=postgres --host=postgres

echo "Compelte ETL"
