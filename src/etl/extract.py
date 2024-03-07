import pandas as pd
import logging

def extract_data(file_path):
    """
    Extract data from the specified CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Extracted data.
    """
    logging.info("Extracting data from file: %s", file_path)
    df = pd.read_csv(file_path)
    logging.info("Data extraction successful.")
    return df
