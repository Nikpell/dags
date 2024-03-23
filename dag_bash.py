from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

# Создадим объект класса DAG
dag =  DAG('dag_bash', schedule_interval=timedelta(days=1), start_date=days_ago(1))

# Создадим несколько шагов, которые будут параллельно исполнять dummy(пустые)команды
t1 = BashOperator(task_id='task_1',
                  bash_command='/airflow-docker/dags/dag1.py',
                  dag=dag)