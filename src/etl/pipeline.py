from extract import extract_data
from transform import transform_data
from load import load_data
from sqlalchemy import create_engine
from src.config import DATABASE_URL, FILE_PATH
import logging

def etl_pipeline(FILE_PATH, DATABASE_URL):
    """
    Execute the ETL pipeline.
   
    Args:
        file_path (str): Path to the input CSV file.
        db_engine (sqlalchemy.engine.base.Engine): Database engine.
    """
    try:
        df = extract_data(FILE_PATH)
        df = transform_data(df)
        load_data(df, DATABASE_URL)
        logging.info("ETL pipeline completed successfully.")
    except Exception as e:
        logging.error("An error occurred during ETL pipeline execution: %s", str(e))
        
if __name__ == '__main__':
    db_engine = create_engine(DATABASE_URL)
    etl_pipeline(FILE_PATH, db_engine) 