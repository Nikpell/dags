from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator


# Создадим объект класса DAG
dag =  DAG('dag', schedule_interval=timedelta(days=1), start_date=days_ago(1))
# Создадим dummy(пустые)команду
t1 = DummyOperator(task_id='task_1', dag=dag)
