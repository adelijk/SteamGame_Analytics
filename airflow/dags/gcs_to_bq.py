from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from pathlib import Path

GCP_PROJECT_ID = Variable.get("GCP_PROJECT_ID")
BUCKET_NAME = Variable.get("BUCKET_NAME")
BQ_RAW_DATASET = Variable.get("BQ_RAW_DATASET")

default_args  = {
    "owner" : "airflow",
    'depends_on_past': False,
    "start_date" : days_ago(1),
}


files_to_tables = {
    'conv_dataset/steam_games.parquet': f'{GCP_PROJECT_ID}.{BQ_RAW_DATASET}.steam_games',
    'conv_dataset/bundle_data.parquet': f'{GCP_PROJECT_ID}.{BQ_RAW_DATASET}.bundle_data',
    'conv_dataset/steam_new.parquet': f'{GCP_PROJECT_ID}.{BQ_RAW_DATASET}.steam_new',
}

with DAG(
    dag_id='gcs_to_bigquery_dynamic_files_autodetect',
    default_args=default_args,
    schedule_interval=None,  
    catchup=False,
) as dag:

    for file_path, table in files_to_tables.items():
        load_task = GCSToBigQueryOperator(
            task_id=f'load_{Path(file_path).stem}_to_bq',  
            bucket=BUCKET_NAME,
            source_objects=[file_path],
            destination_project_dataset_table=table,
            source_format='parquet',
            write_disposition='WRITE_TRUNCATE', 
            create_disposition='CREATE_IF_NEEDED',
            skip_leading_rows=1,  
            autodetect=True,  
        )
