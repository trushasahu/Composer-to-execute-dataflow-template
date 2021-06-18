# Composer-to-execute-dataflow-template
Execute the dataflow template using Composer scheduler

# DF-to-load-CSV-to-BQ
Composer will invoke the dataflow to load CSV data into BigQuery table 

# Steps to load CSV to BQ table

### Create two buckets. 
1-One for landing i.e. Load CSV file into this bucket i.e. third-campus-303308-cf-landing

2-Another for Dataflow to store the temporary files during processing i.e. third-campus-303308-df-bucket

### Create dataset in bigquery
1-create dataset 'airflow_ds' from bigquery console

### Create dataflow template using content in DataFlow folder
1- Put data_ingestion.py & requirements.txt files in the cloud shell 

2- Execute Create_DF_Template_Code.txt scripts in cloud shell to create dataflow template

3- Check in the gs://third-campus-303308-df-bucket/sample-template to verify the dataflow (template_data_ingestion_df) created or not

### Place the csv file (bigmart_data.csv) into the  third-campus-303308-cf-landing  bucket to load data into bigquery table by dataflow job

### Place the Execute_DF_Template_dag.py file into the dag folder.
The dag folder is created in the cloud storage during Composer instance creation.

### You will find a new dag instance(exeute_df_template) for the new file placed in the cloud storage dag folder.

### Manually trigger the dag from UI of airflow which create a dataflow job to load csv file into bigquery table.

### Once Dataflow executed successfully, Please check in Bigquery console
  -The table (airflow_ds.big_mart_df) should be created with the data from csv

  
  
  

