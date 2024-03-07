import logging
from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///C:/Users/h.riabi/OneDrive - NUMERYX/Bureau/Projet/Home_task_1/Home_Task_DE_1/data/databases/database.db'
FILE_PATH = "C:/Users/h.riabi/OneDrive - NUMERYX/Bureau/Projet/Home_task_1/Home_Task_DE_1/data/raw/fashion_dataset.csv"
API_LOG = 'C:/Users/h.riabi/OneDrive - NUMERYX/Bureau/Projet/Home_task_1/Home_Task_DE_1/logs/api_logs.log'
ETL_LOG = 'C:/Users/h.riabi/OneDrive - NUMERYX/Bureau/Projet/Home_task_1/Home_Task_DE_1/logs/etl_logs.log'

logging.basicConfig(filename=API_LOG, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(filename=ETL_LOG, filemode='a', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Connect to the database
def connect_to_database():
    try:
        db_engine = create_engine(DATABASE_URL)
        return db_engine
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

db_engine = connect_to_database()