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
        self.assertEqual(8817.595, rate)

    @patch('bitcoin.get_dollars')
    def test_get_dollars(self, mock_bitcoin, mock_rate):
        mock_rate.side_effect[ 8817.595 ]
        mock_bitcoin.side_effect[ 2 ] 
        dollars = mock_bitcoin * mock_rate
        self.assertEqual(17635.18, dollars)
 
if __name__ == '__main__':
    unittest.main()