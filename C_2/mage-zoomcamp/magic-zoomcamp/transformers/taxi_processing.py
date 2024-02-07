if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    print(data.columns)

    print(f"Preprocessing rows with zero passengers: {data[['passenger_count']].isin([0]).sum()}")
    data = data["passenger_count"] > 0
    print(f"Preprocessing rows with trip distance equal to or less than zero: {data[['trip_distance']].isin([0]).sum()}")
    data = data["trip_distance"] > 0

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date


    columns_actual= data.columns
    columns_snake_case = [col.lower().replace(' ', '_') for col in columns_actual]
    map_columns = dict(zip(columns_actual, columns_snake_case))
    data.rename(columns=map_columns, inplace=True)


    return data


@test
def test_output(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() ==  0, 'The are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() ==  0, 'The are rides with trip distance equal o less than zero'
