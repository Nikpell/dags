import os
import requests




def get():
      data_path = 'data/data.csv'
      os.makedirs(os.path.dirname(data_path))
      url = 'https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/tutorial/pipeline_example.csv'
      respons = requests.request('GET', url)
      with open(data_path, 'w') as file:
            print(respons.text)
            file.write(respons.text)

get()