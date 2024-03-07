import pandas as pd
from sqlalchemy import inspect
import logging

def load_data(df, db_engine):
    """
    Load data into the specified database table.

    Args:
        df (pandas.DataFrame): DataFrame to load.
        db_engine (sqlalchemy.engine.base.Engine): Database engine.
    """
    # Check if table exists in the database
    inspector = inspect(db_engine)
    if 'fashion' in inspector.get_table_names():
        # If the table exists, check if any data is already present
        existing_data = pd.read_sql('SELECT COUNT(*) FROM fashion', db_engine)
        if existing_data.iloc[0, 0] > 0:
            logging.info("Data already exists in the 'fashion' table. Skipping loading.")
            return
    
    # If table does not exist or is empty, append the data
    df.to_sql('fashion', db_engine, if_exists='append', index=False)
    logging.info("Data loading successful.")