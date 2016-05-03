import unittest
from datetime import datetime
from ..stock import Stock

class StockTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")
        self.delta = 0.0001

    def test_price_of_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        """An update should set the price on the stock object
        We will be using the `datetime` module for the timestamp
        """
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        self.assertRaises(ValueError,self.goog.update,datetime(2016,4,28),-1)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2016,4,28),price=10)
        self.goog.update(datetime(2016,4,29),price=8.4)
        self.assertAlmostEqual(8.4,self.goog.price,delta=self.delta)

    def test_stock_price_should_give_latest_desipite_order(self):
        self.goog.update(datetime(2016,4,30),price=8.4)
        self.goog.update(datetime(2016,4,28),price=10)
        self.assertAlmostEqual(8.4,self.goog.price,delta=self.delta)



class StockTrendTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")

    def given_a_series_of_prices(self,prices):
        timestamps = [datetime(2016,4,28),datetime(2016,4,29),datetime(2016,4,30)]
        for timestamp,price in zip(timestamps,prices):
            self.goog.update(timestamp,price)

    def given_a_series_of_timestamps_and_prices(self,timestamps,prices):
        for timestamp,price in zip(timestamps,prices):
            self.goog.update(timestamp,price)


    def test_increasing_trend_is_ture_if_price_increase_for_3_updates(self):
        self.given_a_series_of_prices([8,10,12])
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_decreases(self):
        self.given_a_series_of_prices([8,12,10])
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equal(self):
        self.given_a_series_of_prices([8, 10, 10])
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_true_even_when_disordered_updates(self):
        timestamps = [datetime(2016,4,30),datetime(2016,4,1),datetime(2016,4,14)]
        prices = [20,4,12]
        self.given_a_series_of_timestamps_and_prices(timestamps,prices)
        self.assertTrue(self.goog.is_increasing_trend())

