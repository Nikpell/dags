'''
Добавьте в граф httpSensor который будет обращаться к сайту gb.ru.
Отправьте в чат скриншот кода и логи работы
'''

from airflow import DAG
from datetime import datetime
from airflow.providers.http.sensors.http import HttpSensor
    
    
dag = DAG( 'http_sensor' , description= 'http_senor',
    schedule_interval= '0 12 * * *' ,
    start_date=datetime( 2023 , 1 , 1
    ), catchup= False )

task_http_sensor_check = HttpSensor(
    task_id="http_sensor_check",
    http_conn_id="https://gb.ru",
    endpoint="https://gb.ru",
    request_params={},
    response_check=lambda response: "httpbin" in response.text,
    poke_interval=5,
    dag=dag,)

