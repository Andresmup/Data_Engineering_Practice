import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    url_10 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    url_11 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    url_12 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'

    taxi_dtypes = {
        'VendorID' : pd.Int64Dtype(),
        'passenger_count' : pd.Int64Dtype(),
        'trip_distance' : float,
        'RatecodeID' : pd.Int64Dtype(),
        'store_and_fwd_flag' : str,
        'PULocationID' : pd.Int64Dtype(),
        'DOLocationID' : pd.Int64Dtype(),
        'payment_type' : pd.Int64Dtype(),
        'fare_amount' : float,
        'extra' : float,
        'mta_tax' : float,
        'tip_amount' : float,
        'tolls_amount' : float,
        'improvement_surcharge' : float,
        'total_amount' : float,
        'congestion_surcharge' : float
    }
    parse_dates = ['lpep_pickup_datetime','lpep_dropoff_datetime']

    df_10 = pd.read_csv(url_10, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
    df_11 = pd.read_csv(url_11, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
    df_12 = pd.read_csv(url_12, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)

    df_concatenated = pd.concat([df_10, df_11, df_12], ignore_index=True)

    return df_concatenated




@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
