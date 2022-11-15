from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

#from my_module_func.module_func import MyFuncDAG


DEFAULT_ARGS = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
    'start_day': days_ago(0, 0, 0, 0, 0)
}

def do_sth():
    test = print("hi")#MyFuncDAG()


with DAG(
        dag_id='ingest_data_from_OpenSkyApi_v1',
        default_args=DEFAULT_ARGS,
        description='This is a dag that logs into https://opensky-network.org/api/states/all, and then prints all '
                    'the states',
        schedule="@daily",
        catchup=False,
        start_date=days_ago(0, 0, 0, 0, 0),
) as dag:
    jobing = PythonOperator(
        task_id='my_module_func',
        python_callable=do_sth
    )


jobing
