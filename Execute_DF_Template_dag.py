"""
Example Airflow DAG for Google Cloud Dataflow service.
loading cloud storage csv file into bigquery table.
"""

import os

from airflow import DAG
from airflow.providers.google.cloud.operators.dataflow import DataflowTemplatedJobStartOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

#PROJECT_ID = os.environ.get("GCP_PROJECT_ID", 'third-campus-303308')
#GCS_OUTPUT = os.environ.get('GCP_DATAFLOW_GCS_OUTPUT', 'gs://third-campus-303308-df-bucket/temp-location')

#path of the dataflow template on google storage bucket
template = "gs://third-campus-303308-df-bucket/sample-template/template_data_ingestion_df"
inputFile = "gs://third-campus-303308-cf-landing/bigmart_data.csv"
bq_table_name = "airflow_ds.big_mart_df"
#user defined parameters to pass to the dataflow pipeline job
parameters = {
		'inputFile': inputFile, 'bq_table': bq_table_name
	}


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2), #datetime(2019, 6, 30),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='exeute_df_template',
	catchup=False,
	default_args=default_args,
    schedule_interval=None
)

execute_df_template_job = DataflowTemplatedJobStartOperator(
        task_id="execute-df-template-job",
        template=template,
        parameters=parameters,
        location='europe-west3',
		dag=dag,
    )

execute_df_template_job
