class HashMap:
    numCompanies = 0;

    def __init__(self):
        self.arr = [-1 for x in range(201130)]

    def insert(self, date, value):
        index = date-20000101
        self.arr[index] = value

    def search(self, date):
        index = int(date)-20000101
        return self.arr[index]

