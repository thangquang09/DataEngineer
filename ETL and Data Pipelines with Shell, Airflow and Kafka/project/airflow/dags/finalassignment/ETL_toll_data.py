# Import Libraries
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

# Expand the project folder path
PROJECT_FOLDER = os.path.expanduser('~/project/airflow/dags/finalassignment')

# Define DAG arguments
default_args = {
    'owner': 'etl_toll_data_bash',
    'start_date': datetime(2024, 8, 30),
    'email': 'thangquangly0909@gmail.com',
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,  # Corrected from 'retires' to 'retries'
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    dag_id='ETL_toll_data',
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    description='ETL_toll_data pipeline, final project'
)

# Tasks

## unzip data
unzip_data = BashOperator(
    task_id='unzip',
    bash_command=f'tar -xzf {PROJECT_FOLDER}/tolldata.tgz -C {PROJECT_FOLDER}',
    dag=dag
)

## extract data from csv
extract_data_from_csv = BashOperator(
    task_id='extract_data_csv',
    bash_command=f'cut -d "," -f1-4 {PROJECT_FOLDER}/vehicle-data.csv > {PROJECT_FOLDER}/csv_data.csv',
    dag=dag
)

## extract data from tsv
extract_data_from_tsv = BashOperator(
    task_id='extract_data_tsv',
    bash_command=f"cat {PROJECT_FOLDER}/tollplaza-data.tsv | tr '\t' ',' | cut -d ',' -f5-7 | tr -d '\r' > {PROJECT_FOLDER}/tsv_data.csv",
    dag=dag
)

## extract data from fixed width
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command=f"rev {PROJECT_FOLDER}/payment-data.txt | tr -s ' ' | cut -d ' ' -f1-2 | rev | tr ' ' ',' | tr -d '\r' > {PROJECT_FOLDER}/fixed_width_data.csv",
    dag=dag
)

## consolidate data
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command=f"paste -d ',' {PROJECT_FOLDER}/csv_data.csv {PROJECT_FOLDER}/tsv_data.csv {PROJECT_FOLDER}/fixed_width_data.csv > {PROJECT_FOLDER}/extracted_data.csv",
    dag=dag
)

## transform data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command=f"awk -F ',' -v OFS=',' '{{ $4=toupper($4); print }}' {PROJECT_FOLDER}/extracted_data.csv > {PROJECT_FOLDER}/staging/transformed_data.csv",
    dag=dag
)

# Task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
