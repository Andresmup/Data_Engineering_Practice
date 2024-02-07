if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    print(f"Preprocessing rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing rows with trip distance equal to or less than zero: {data['trip_distance'].isin([0]).sum()}")

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    existing_values = data['VendorID'].unique()


    column_mapping = {
        'VendorID': 'vendor_id',
        'lpep_pickup_datetime': 'lpep_pickup_datetime',  
        'lpep_dropoff_datetime': 'lpep_dropoff_datetime',  
        'store_and_fwd_flag': 'store_and_fwd_flag',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id',
        'passenger_count': 'passenger_count',
        'trip_distance': 'trip_distance',
        'fare_amount': 'fare_amount',
        'extra': 'extra',
        'mta_tax': 'mta_tax',
        'tip_amount': 'tip_amount',
        'tolls_amount': 'tolls_amount',
        'ehail_fee': 'ehail_fee',
        'improvement_surcharge': 'improvement_surcharge',
        'total_amount': 'total_amount',
        'payment_type': 'payment_type',
        'trip_type': 'trip_type',
        'congestion_surcharge': 'congestion_surcharge'
    }   
    data.rename(columns=column_mapping, inplace=True)

    print(f"Nº of columns renamed: 4")

    data_filtered = data[data["passenger_count"] > 0]
    data_filtered["trip_distance"] = data_filtered["trip_distance"].where(data_filtered["trip_distance"] > 0)

    print(data_filtered.columns)
    print(data_filtered['vendor_id'].unique())
    #assert data_filtered['vendor_id'].isin([existing_values]).all(), 'vendor_id should be one of the existing values'
    
    return data_filtered


@test
def test_output(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() ==  0, 'The are rides with zero passengers'
@test
def test_output(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() ==  0, 'The are rides with trip distance equal o less than zero'