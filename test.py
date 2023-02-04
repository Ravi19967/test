"""
### DATA-1234
"""
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

name='test'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def output_sql(sql_code: str):
    print(sql_code)

dag = DAG(
            name,
            start_date=datetime(2019, 1, 1),
            max_active_runs=1,
            schedule_interval='0 12 8-14,22-28 * 6',
            default_args=default_args,
            catchup=False,
            doc_md = __doc__,
            tags = ['created from slack']
        )

t0 = DummyOperator(task_id='start')

t1 = PythonOperator(
        task_id="output_sql_test",
        python_callable=output_sql,
        op_kwargs= {'sql_code': 'SELECT 1'}
    )

t0 >> t1