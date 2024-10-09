from airflow import DAG
from airflow.utils.dates import days_ago
from data_cleaner_parquet import convert_to_parquet
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.operators.bash import BashOperator
from airflow.models import Variable
import datetime
import os  

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),

}

BUCKET_NAME = Variable.get("BUCKET_NAME")
DATA_FOLDER = "/opt/airflow/conv_dataset"
GOOGLE_APPLICATION_CREDENTIALS =Variable.get("GOOGLE_APPLICATION_CREDENTIALS")


with DAG(
    dag_id='create_gcs_bucket2',
    default_args=default_args,
    schedule_interval=None,  
    catchup=False,
    tags=['steamgame'],
) as dag:

    convert_steam_games = PythonOperator(
        task_id='convert_steam_games',
        python_callable=convert_to_parquet,
        op_args=['/opt/airflow/dataset/steam_games.json', '/opt/airflow/conv_dataset/steam_games.parquet'],
        op_kwargs={'process': True},
    )

    convert_steam_new = PythonOperator(
        task_id='convert_steam_new',
        python_callable=convert_to_parquet,
        op_args=['/opt/airflow/dataset/steam_new.json', '/opt/airflow/conv_dataset/steam_new.parquet'],
    )

    convert_bundle_data = PythonOperator(
        task_id='convert_bundle_data',
        python_callable=convert_to_parquet,
        op_args=['/opt/airflow/dataset/bundle_data.json', '/opt/airflow/conv_dataset/bundle_data.parquet'],
    )

    auth_task = BashOperator(
            task_id='authenticate_service_account', 
            bash_command=f"gcloud auth activate-service-account --key-file={GOOGLE_APPLICATION_CREDENTIALS}",
        )


    upload_dataset_task = BashOperator(
        task_id='upload_dataset_to_gcs',
        bash_command=f"gsutil -m cp -r {DATA_FOLDER} gs://{BUCKET_NAME}/"
    )
    convert_steam_games >> convert_steam_new >> convert_bundle_data >> auth_task >> upload_dataset_task
