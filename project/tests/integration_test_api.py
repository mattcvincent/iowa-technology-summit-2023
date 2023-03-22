import unittest
import os
from app.api import ApiClient
from dotenv import load_dotenv


class TestIntegrationApiClient(unittest.TestCase):
    def setUp(self):
        load_dotenv() # Load environment variables
        self.client = ApiClient()

    def test_fetch_large_data(self):
        # Call the fetch_data method to get a large amount of data
        data = self.client.fetch_data(stopAfter=3,dateFrom="2023-03-10")

        # Test that the response is valid
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        # ... more assertions as needed
