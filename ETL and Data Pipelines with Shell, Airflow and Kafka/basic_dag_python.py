# Import các thư viện cần thiết
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

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

# Khởi tạo DAG
dag = DAG(
  'example_dag',
  default_args=default_args,
  description='Một ví dụ về DAG trong Apache Airflow',
  schedule_interval=timedelta(days=1),
)

# Định nghĩa các nhiệm vụ trong DAG
## task1: in ra Hello World!
task1 = BashOperator(
  task_id='print_hello',
  bash_command='echo "Hello World!"',
  dag=dag
)

## task2: đếm số file trong thư mục /tmp
task2 = BashOperator(
  task_id='count_files',
  bash_command='ls -l /tmp | wc -l',
  dag=dag
)

# Định nghĩa thứ tự thực hiện các task
task1 >> task2