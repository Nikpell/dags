from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.dummy import DummyOperator
 
dag = DAG('dag_doc_1',schedule_interval=timedelta(days=1), start_date=days_ago(1))
t1 = DummyOperator(task_id='task_1', dag=dag)
t2 = DummyOperator(task_id='task_2',dag=dag)
t3 = DummyOperator(task_id='task_3',dag=dag)
t4 = DummyOperator(task_id='task_4',dag=dag)


t1.doc_md = "Task Documentations :)"
dag.doc_md = __doc__ 
dag.doc_md = "Dag Documentations :)"
 
t1 >> t2 >> [t3, t4]