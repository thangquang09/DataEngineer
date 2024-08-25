# import thư viện
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import requests

# Định nghĩa các đối số mặc định cho DAG
default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':datetime(2024, 8, 25),
    'email_on_failure':False,
    'email_on_retry':False,
    'retires':1,
    'retry_delay':timedelta(minutes=5),
}

input_file = 'web-server-access-log.txt'
extracted_file = 'extracted-data.txt'
transformed_file = 'transformed-data.txt'
output_file = 'output-data.txt'

# Khởi tạo DAG
dag = DAG(
    'server_access_log_preprocessing',
    default_args=default_args,
    description='Xử lý file log truy cập server',
    schedule_interval=timedelta(days=1),
)

def download_file():
    url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt'
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(input_file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"File downloaded successfully: {input_file}")

def extract():
    global input_file, transformed_file
    print("Extracting")
    with open(input_file, 'r') as infile, open(extracted_file, 'w') as outfile:
        for line in infile:
            fileds = line.split('#')
            print(fileds)

download_file()
extract()