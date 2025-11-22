# imports
import unittest
from datetime import datetime

# Test class
class TestInputs(unittest.TestCase):
    def setUp(self):
        #Set up some example inputs to work with. These can be changed whenever needed
        self.symbol = "AAPL"
        self.chart = "1"
        self.time = "3"
        self.start = "2025-01-01"
        self.end = "2025-12-31"

    #Test self.symbol
    def test_symbol(self):
        result = self.symbol.isalpha() and self.symbol.isupper() and 1 < len(self.symbol) < 7
        self.assertEqual(result, True)

    #test chart
    def test_chart(self):
        result = self.chart in ["1", "2"]
        self.assertEqual(result, True)

    #test time
    def test_time(self):
        result = self.time in ["1", "2", "3", "4"]
        self.assertEqual(result, True)

    #test start daet
    def test_start(self):
        try:
            datetime.strptime(self.start, "%Y-%m-%d")
            result = True
        except:
            result = False
        self.assertEqual(result, True)

    #test end date
    def test_end(self):
        try:
            datetime.strptime(self.end, "%Y-%m-%d")
            result = True
        except:
            result = False
        self.assertEqual(result, True)

#run unit test
if __name__ == "__main__":
    unittest.main()