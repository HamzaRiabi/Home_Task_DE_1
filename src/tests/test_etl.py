import unittest
import pandas as pd
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from src.config import FILE_PATH, db_engine
from sqlalchemy import text
class TestETLPipeline(unittest.TestCase):

    def test_extract_data(self):
        df = extract_data(FILE_PATH)
        self.assertIsInstance(df, pd.DataFrame)

    def test_transform_data(self):
        df = pd.DataFrame({'A': [1, 2, None], 'B': [4, 5, 6]})
        transformed_df = transform_data(df)
        self.assertEqual(transformed_df.shape, (2, 2))

    def test_load_data(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        with db_engine.connect() as connection:
            connection.execute(text('DROP TABLE IF EXISTS fashion'))
            df.to_sql('fashion', connection, if_exists='fail')
        load_data(df, db_engine)
        with db_engine.connect() as connection:
            result = connection.execute(text('SELECT A, B FROM fashion'))
            data = [dict(zip(result.keys(), row)) for row in result]
        self.assertEqual(data, [{'A': 1, 'B': 4}, {'A': 2, 'B': 5}, {'A': 3, 'B': 6}])

if __name__ == '__main__':
    unittest.main()