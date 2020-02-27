import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestExchangeRates(TestCase):

    @patch('bitcoin.get_bitcoin_rate')
    def test_get_bitcoin_rate(self, mock_rates):
        mock_rate = 8817.595
        example_api_response = {'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '8,817.5950', 'description': 'United States Dollar', 'rate_float': mock_rate}}}
        mock_rates.side_effect = [ example_api_response ]
        rate = bitcoin.get_bitcoin_rate(example_api_response)
        self.assertEqual(8817.59, rate)

    if __name__ == '__main__':
        unittest.main()