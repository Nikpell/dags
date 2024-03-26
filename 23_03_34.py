from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
import pandas as pd


def f_callable(url, f_name):
  smth = pd.read_csv(url)
  smth.to_csv(f_name)

def merge_data(url1, url2, key):
  data1 = pd.read_csv(url1)
  data2 = pd.read_csv(url2)
  data1.rename(columns = {'currency_to':'code', 'currency_from':'base'}, inplace = True )
  df2 = data2.merge(data1, left_on=key, right_on=key, how='inner')
  df = df2[['date', 'code', 'base', 'amount', 'value']]
  return df

dag = DAG('157497468', schedule_interval=timedelta(days=1), start_date=days_ago(1))
  
t1 = PythonOperator(task_id='download_file_1', python_callable=f_callable, 
                    op_kwargs={'url': 'https://raw.githubusercontent.com/datanlnja/airflow_course/main/excangerate/2021-01-01.csv',
                    'f_name': '/usr/local/airflow/dags/sandbox/157497468/exc-2021-01-01.csv'},
                    dag=dag)

t2 = PythonOperator(task_id='download_file_2', python_callable=f_callable,
                      op_kwargs={'url': 'https://raw.githubusercontent.com/datanlnja/airflow_course/main/data/2021-01-01.csv',
                      'f_name': '/usr/local/airflow/dags/sandbox/157497468/ma-2021-01-01.csv'},
                    dag=dag)



t1 >> t2