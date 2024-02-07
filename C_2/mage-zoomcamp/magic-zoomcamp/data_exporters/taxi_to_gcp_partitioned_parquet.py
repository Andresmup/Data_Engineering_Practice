import pyarrow as pa
import pyarrow.parquet as pq
import os


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/dataengineeringcourse-0001-a870f0fc2f2b.json'
bucket_name = 'mage-zoomcamp-andres'
proyect_id = 'dataengineeringcourse-0001'
table_name  = 'green_taxi'
schema = 'mage'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    if_exists='replace',  # Specify resolution policy if table name already exists
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        
        filesystem = gcs
    )

