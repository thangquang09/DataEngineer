import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')
path = 'Department.csv'
attribute_names = ["DEP_ID", "DEP_NAME", "MANAGER_ID", "LOC_ID"]
table_name = "DEPARTMENT"
department_df = pd.read_csv(path, names=attribute_names)
department_df.to_sql(table_name, conn, if_exists='replace', index=False)

def query(query_statement, conn):
    query_output = pd.read_sql(query_statement, conn)
    print(query_statement)
    print(query_output)

statement = f"SELECT COUNT(*) FROM {table_name}"
query(statement, conn)

# append new instance
data_dict = {
    attribute_names[0]: ['9'],
    attribute_names[1]: ['Quality Assurance'],
    attribute_names[2]: ['30010'],
    attribute_names[3]: ['L0010']
}
append_df = pd.DataFrame(data_dict)
append_df.to_sql(table_name, conn, if_exists='append', index=False)

# task 4
# view all entries
query1 = f"SELECT * FROM {table_name}"
query2 = f"SELECT DEP_NAME FROM {table_name}"
query3 = f"SELECT COUNT(*) FROM {table_name}"

query(query1, conn)
query(query2, conn)
query(query3, conn)
conn.close()