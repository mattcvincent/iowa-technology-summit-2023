import pandas as pd
import tempfile
import unittest
from app.transform import DataTransform
import pandas as pd
from pandas.testing import assert_frame_equal

class TestDataTransform(unittest.TestCase):
    def setUp(self):
        self.transform = DataTransform()
        
    def test_flatten_data(self):
        input_data = [
            {
                "userId": 1,
                "records": [
                    {
                        "taskId": 116,
                        "time": 120
                    },
                    {
                        "taskId": 135,
                        "time": 105
                    }
                ],
                "dayOffset": 0,
                "date": "2023-03-01"
            },
            {
                "userId": 15,
                "records": [
                    {
                        "taskId": 116,
                        "time": 90
                    },
                    {
                        "taskId": 117,
                        "time": 150
                    },
                    {
                        "taskId": 118,
                        "time": 165
                    }
                ],
                "dayOffset": 0,
                "date": "2023-03-01"
            }
        ]
        
        expected_output = pd.DataFrame({
            "userId": [1, 1, 15, 15, 15],
            "taskId": [116, 135, 116, 117, 118],
            "time": [120, 105, 90, 150, 165],
            "dayOffset": [0, 0, 0, 0, 0],
            "date": ["2023-03-01", "2023-03-01", "2023-03-01", "2023-03-01", "2023-03-01"]
        })
        
        actual_output = self.transform.flatten_data(input_data)
        
        assert_frame_equal(actual_output[expected_output.columns], expected_output, check_dtype=False)
        
    def test_save_to_parquet(self):
        # create example data frame
        data = {
            "userId": [1, 2, 3],
            "taskId": [116, 117, 118],
            "time": [120, 105, 90],
            "dayOffset": [0, 0, 0],
            "date": ["2023-03-01", "2023-03-01", "2023-03-01"]
        }
        df = pd.DataFrame(data)
        
        # create temp file and save to parquet
        with tempfile.NamedTemporaryFile() as f:
            filename = f.name
            self.transform.save_to_parquet(df, filename)
            
            # read parquet file back in and compare to original data frame
            df_from_parquet = pd.read_parquet(filename)
            pd.testing.assert_frame_equal(df, df_from_parquet, check_dtype=False)
