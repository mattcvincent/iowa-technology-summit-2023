import requests
from unittest.mock import patch, Mock, call
import unittest
from app.api import ApiClient
from dotenv import load_dotenv
import responses
import os

class TestApiClient(unittest.TestCase):

    def setUp(self):
        load_dotenv() # Load environment variables
        self.client = ApiClient()

    def test_get_data(self):
        # Test that fetch_data does not return none.
        data = self.client.fetch_data()
        self.assertIsNotNone(data)

    @responses.activate
    def test_fetch_data_params(self):
        # Mock the API response
        responses.add(
            responses.GET,
            f"{os.environ['ACTITIME_URL']}timetrack?",
            json={
                'data': [
                    {
                        'userId': 1,
                        'records': [
                            {'taskId': 4, 'time': 1},
                            {'taskId': 5, 'time': 2},
                            {'taskId': 6, 'time': 3},
                        ],
                        'approved': True,
                        'dayOffset': 0,
                        'date': '2022-01-01',
                    },
                    # ... more time-track records ...
                ],
            },
        )

        # Call the fetch_data method with some query parameters
        data = self.client.fetch_data(userIds='1,2,3', taskIds='4,5,6', projectIds='7,8,9', dateFrom='2022-01-01', dateTo='2022-01-31')

        # Test that the URL constructed by requests.get is correct
        self.assertEqual(
            responses.calls[0].request.url,
            f"{os.environ['ACTITIME_URL']}timetrack?dateFrom=2022-01-01&dateTo=2022-01-31&stopAfter=1000&userIds=1%2C2%2C3&taskIds=4%2C5%2C6&projectIds=7%2C8%2C9",
            "Expected requests.get to be called with the correct URL",
        )

        # Test that the response is parsed correctly
        self.assertIsInstance(data, list)
        # self.assertGreater(len(data), 0)
        # ... more assertions as needed

    @patch('requests.get')
    def test_fetch_data_pagination(self, mock_requests):
        # Mock the response for the first call
        response_1 = Mock()
        response_1.ok = True
        response_1.json.return_value = {
            'data': [
                {'taskId': 1, 'time': 1},
                {'taskId': 2, 'time': 2},
                {'taskId': 3, 'time': 3},
            ],
            'nextDateFrom': '2023-03-01'
        }

        # Mock the response for the second call
        response_2 = Mock()
        response_2.ok = True
        response_2.json.return_value = {
            'data': [
                {'taskId': 4, 'time': 4},
                {'taskId': 5, 'time': 5},
            ]
        }

        # Set the side_effect to return the first mock object for the first call and the second mock object for the second call
        mock_requests.side_effect = [response_1, response_2]

        # Create an instance of the ApiClient class
        client = ApiClient()

        # Call the fetch_data method with stopAfter=3
        data = client.fetch_data(stopAfter=3)

        # Assert that the mock object was called twice with the correct parameters
        mock_requests.assert_has_calls([
            call(
                f"{client.url}timetrack",
                headers={"Content-Type": "application/json"},
                auth=(client.username, client.password),
                params={'dateFrom': '2023-03-01', 'dateTo': '3000-12-31', 'stopAfter': 3}
            )
        ])

        # Assert that the data returned by the fetch_data method is correct
        self.assertEqual(data, [
            {'taskId': 1, 'time': 1},
            {'taskId': 2, 'time': 2},
            {'taskId': 3, 'time': 3},
            {'taskId': 4, 'time': 4},
            {'taskId': 5, 'time': 5},
        ])

    @responses.activate
    def test_fetch_data_raises_for_status(self):
        # Mock the API response to return a 404 error
        responses.add(
            responses.GET,
            f"{os.environ['ACTITIME_URL']}timetrack",
            status=404,
        )

        # Call the fetch_data method
        with self.assertRaises(requests.exceptions.HTTPError):
            self.client.fetch_data()
