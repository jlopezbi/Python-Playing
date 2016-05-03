from bisect import bisect_left,insort_left

class Stock(object):
    def __init__(self,symbol):
        self.symbol = symbol
        self.price_history = []
        self.dates = []

    @property
    def price(self):
        return self.price_history[-1] \
                if self.price_history else None

    def update(self,timestamp,price):
        if price < 0:
            raise ValueError("price should not be negative")
        insort_left(self.dates,timestamp)
        index = bisect_left(self.dates,timestamp)
        self.price_history.insert(index,price)

    def is_increasing_trend(self):
        return self.price_history[-3] < \
                self.price_history[-2] < self.price_history[-1]


