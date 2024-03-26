"""
Создайте новый пайплайн. Скачайте файл ССЫЛКА. Сделайте пайплайн 
который будет читать файл, выполнять удаление дубликатов и загружать
очищенные данные в базу данных postgress после этого отправлять письмо
с количеством записей добавленных в базу данных.
Ссылка на файл: 
https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/tutorial/pipeline_example.csv

"""

import os
import requests
from airflow.decorators import task
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator


dag = DAG( 'lesson_7' , description= 'get_file',
    schedule_interval= '0 12 * * *' ,
    start_date=datetime( 2023 , 1 , 1
    ), catchup= False )



def get():
      data_path = 'home/airflow/dags/smth.csv'
      #os.makedirs(os.path.dirname(data_path), exist_ok=True)
      url = 'https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/tutorial/pipeline_example.csv'
      respons = requests.request('GET', url)
      with open('home/airflow/dags/smth.csv', 'w') as file:
            file.write(respons.text)
      

task1 =  PythonOperator(task_id= 'get_file' , python_callable=get, dag=dag)

      