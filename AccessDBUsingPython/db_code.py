import sqlite3
import pandas as pd
# connect to database
conn = sqlite3.connect("STAFF.db")

table_name="INSTRUCTOR"
attribute_list=["ID", "FNAME", "LNAME", "CITY", "CCODE"]

file_path="INSTRUCTOR.csv"
df = pd.read_csv(file_path, names=attribute_list)

# create and load the table to database 
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')

# query some statement
def query(query_statement, conn):
    query_output = pd.read_sql(query_statement, conn)
    print(query_statement)
    print(query_output)

# viewing only FNAME column of data
query_statement = f"SELECT FNAME FROM {table_name}"
query(query_statement, conn)
# viewing total number of entries in the table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query(query_statement, conn)

# append new instance to table
data_dict = {
    'ID': [100],
    'FNAME': ['John'],
    'LNAME': ['Doe'],
    'CITY': ['Paris'],
    'CCODE': ['FR']
}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully!')

query_statement = f"SELECT * FROM {table_name}"
query(query_statement, conn)

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query(query_statement, conn)

conn.close()