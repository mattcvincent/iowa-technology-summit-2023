import os
import unittest
from unittest.mock import patch
from util import lake_loader
import pandas as pd
from pandas.testing import assert_frame_equal
from app.api import ApiClient

class TestLakeLoader(unittest.TestCase):
    
    @patch.object(ApiClient, 'fetch_data')
    def test_main(self, mock_fetch_data):
        # Define test data
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
        mock_fetch_data.return_value = input_data

        # Call main() to process test data
        lake_loader.main()

        # Load saved data from file
        output_file = "flattened_timetrack_data.parquet"
        self.assertTrue(os.path.isfile(output_file))
        actual_output = pd.read_parquet(output_file)

        # Define expected output
        expected_output = {
            "userId": [1, 1, 15, 15, 15],
            "taskId": [116, 135, 116, 117, 118],
            "time": [120, 105, 90, 150, 165],
            "dayOffset": [0, 0, 0, 0, 0],
            "date": ["2023-03-01", "2023-03-01", "2023-03-01", "2023-03-01", "2023-03-01"]
        }

        # Verify output data matches expected data
        assert_frame_equal(actual_output[expected_output.keys()], pd.DataFrame(expected_output), check_dtype=False)
