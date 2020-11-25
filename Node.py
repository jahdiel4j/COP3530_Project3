class Node:
    def __init__(self, date, stock_value):
        self.date = date
        self.stock_value = stock_value
        self.left = None
        self.right = None
        self.height = 1