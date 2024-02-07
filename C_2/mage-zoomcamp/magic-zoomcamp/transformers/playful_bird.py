import pandas as pd
from datetime import datetime


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(data.sort_values('lpep_pickup_date', ascending=False)['lpep_pickup_date'].head(10))

    print(data.sort_values('lpep_pickup_date', ascending=False)['lpep_pickup_date'].tail(10))

    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_date']).dt.date
    filtered_data = data[(data['lpep_pickup_date'] >= datetime(2020, 10, 1).date()) & (data['lpep_pickup_date'] <= datetime(2020, 12, 31).date())]
    unique_days_count = filtered_data['lpep_pickup_date'].nunique()
    print(f"Número de días únicos en octubre, noviembre y diciembre del 2020: {unique_days_count}")

    unique_days_count = data['lpep_pickup_date'].nunique()
    print(f"Número de días únicos: {unique_days_count}")
    

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
