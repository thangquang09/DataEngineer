# import thư viện
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import requests
import os

folder_path = '/home/thangquang/CODE/DataEngineer/ETL and Data Pipelines with Shell, Airflow and Kafka'

# Định nghĩa các đối số mặc định cho DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

input_file = os.path.join(folder_path, 'web-server-access-log.txt')
extracted_file = os.path.join(folder_path, 'extracted-data.txt')
transformed_file = os.path.join(folder_path, 'transformed-data.txt')
output_file = os.path.join(folder_path, 'output-data.txt')

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
    print("Extracting")
    with open(input_file, 'r') as infile, open(extracted_file, 'w') as outfile:
        for line in infile:
            fields = line.split('#')
            if len(fields) >= 4:
                field_1 = fields[0]
                field_4 = fields[3]
                outfile.write(field_1 + '#' + field_4 + '\n')

def transform():
    print("Transforming")
    with open(extracted_file, 'r') as infile, open(transformed_file, 'w') as outfile:
        for line in infile:
            processed_line = line.upper()
            outfile.write(processed_line + '\n')

def load():
    print("Loading")
    with open(transformed_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line + '\n')

def check():
    print("Checking")
    with open(output_file, 'r') as f:
        lines = f.readlines()
        for line in lines[:5]:
            print(line)

# Tạo các task
download_task = PythonOperator(
    task_id='download_file',
    python_callable=download_file,
    dag=dag,
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load,
    dag=dag,
)

check_task = PythonOperator(
    task_id='check_data',
    python_callable=check,
    dag=dag,
)

# Xác định thứ tự thực hiện cá

download_task >> extract_task >> transform_task >> load_task >> check_task