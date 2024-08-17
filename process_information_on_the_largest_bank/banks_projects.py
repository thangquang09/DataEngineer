import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attbts_extract = ["Name", "MC_USD_Billion"]
table_attbts_final = ["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]
csv_path = "./Largest_banks_data.csv"
db_name = "Banks.db"
table_name = "Largest_banks"
log_file = "code_log.txt"

rate_df = pd.read_csv("exchange_rate.csv")
key = rate_df['Currency']
value = rate_df['Rate']
rate_dict = dict(zip(key, value))

def log_progress(message):
    time_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(time_format)
    with open(log_file, 'a') as f:
        f.write(timestamp + " : " + message + "\n")

def extract(url, table_attbts):
    page = requests.get(url)
    data = BeautifulSoup(page.text, 'html.parser')
    tables = data.find_all('tbody')
    # tables[0] is the table we need to find
    rows = tables[0].find_all('tr')
    df = pd.DataFrame(columns=table_attbts_extract)
    for row in rows:
        col = row.find_all('td')
        if(len(col) != 0):
            name, market_cap = col[1].text.strip(), col[2].text.strip()
            # print(name, market_cap, sep = "\t")
            data_dict = {table_attbts_extract[0]: name, table_attbts_extract[1]: market_cap}
            per_df = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, per_df], ignore_index=True)

    return df

def transform(df):
    market_cap_list = [float(x) for x in df['MC_USD_Billion'].to_list()] # convert from str to float
    format_str = "MC_{}_Billion"
    for key, value in rate_dict.items():
        df[format_str.format(key)] = [np.round(x * value, 2) for x in  market_cap_list]
    return df

def load_to_csv(df, csv_path):
    df.to_csv(csv_path)

def load_to_db(df, sql_connection):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

if __name__ == "__main__":
    sql_connection = sqlite3.connect(db_name)
    log_progress("Connected to Database! Ready for process.")

    banks_df = extract(url, table_attbts_extract)
    log_progress("Data Extracted Completely, ready for tranformation.")

    banks_df = transform(banks_df)
    log_progress("Data Transformated Completely, loading to csv.")

    load_to_csv(banks_df, csv_path)
    log_progress("Loaded to csv, loading to database.")

    load_to_db(banks_df, sql_connection)
    log_progress("Data Loading Succesfully, loading query statement.")

    sql_statement = f"SELECT * FROM {table_name} WHERE MC_USD_Billion > 150"
    run_query(sql_statement, sql_connection)

    log_progress("Process End.")

    sql_connection.close()