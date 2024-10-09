from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),

}

with DAG(
    dag_id='transform_data',
    default_args=default_args,
    schedule_interval=None,  
    catchup=False,
) as dag:

    run_dbt_task = BashOperator(
        task_id="run_dbt_task",
        bash_command="cd /dbt && dbt deps && dbt run --profiles-dir ."
    )