"""
1. Создайте новый граф. Добавьте в него BashOperator, 
который будет генерировать рандомное число и печатать 
его в консоль.

2. Создайте PythonOperator, который генерирует 
рандомное число, возводит его в квадрат и выводит 
в консоль исходное число и результат.

3. Сделайте оператор, который отправляет запрос к 
https://goweather.herokuapp.com/weather/"location" 
(вместо location используйте ваше местоположение).

4. Задайте последовательный порядок выполнения 
операторов.
"""

from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from random import randint
from airflow.operators.python_operator import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.python import get_current_context
from airflow.providers.http.operators.http import SimpleHttpOperator

def generate_randint():
      num = randint(0, 32_767)
      return f'{num} & {num**2}'



dag = DAG( 'task_6', description= 'See description',
    schedule_interval= '0 12 * * *' ,
    start_date=datetime( 2023 , 1 , 1
    ), catchup= False)


put_random_down_from_bash =  BashOperator(
      task_id= 'task_start', 
      bash_command="echo $RANDOM", 
      dag=dag)

task2 = PythonOperator(
      task_id='task_2',
      python_callable=generate_randint,
      dag=dag)

check_file = SimpleHttpOperator(
    method='GET',
    endpoint='"Perm"',
    task_id='check_file',
    http_conn_id='task_6'
)

put_random_down_from_bash >> task2 >> check_file

