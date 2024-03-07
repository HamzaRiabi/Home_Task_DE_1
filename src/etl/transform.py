import pandas as pd
import logging

def transform_data(df):
    """
    Perform data transformation by dropping NaN values.

    Args:
        df (pandas.DataFrame): Input DataFrame.

    Returns:
        pandas.DataFrame: Transformed DataFrame.
    """
    logging.info("Transforming data...")
    df = df.dropna()
    logging.info("Data transformation successful.")
    return df
