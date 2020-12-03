from HashMap import HashMap
import csv

class HashSetup:
    # Dictionary/Map of Company Hashmaps
    companies_list = {}
    # List of companies in order of the CSV file's columns
    ordered_companies = []

    """ Covert given "date" string into a formatted int (for insertion into AVL Tree) """

    def convert_date(self, date):
        # MM/DD/YYYY -> YYYYMMDD
        l = date.split("/")

        month = l[0]
        if len(month) == 1:
            month = "0" + month
        day = l[1]
        if len(day) == 1:
            day = "0" + day
        year = l[2]

        str_date = year + month + day

        return int(str_date)

    """ Fills in companies_list with the CSV file data """

    def initialize_companies_map(self):
        csv_file = open('COP3530 Project 3 Data.csv')
        reader = csv.reader(csv_file)
        companies = next(reader)

        for i in range(len(companies)):
            # Index 0 in the 1st row is where it says "Date"
            if i != 0:
                self.companies_list[companies[i]] = HashMap()
                self.ordered_companies.append(companies[i])

        for row in reader:
            # 1st Column contains the dates
            date = self.convert_date(row[0])
            i = 1

            for company in self.ordered_companies:
                # If a cell contains #N/A, put its stock value as a negative number (impossible)
                try:
                    self.companies_list[company].insert(date, float(row[i]))
                except ValueError:
                    self.companies_list[company].insert(date, -1)

                i += 1

        csv_file.close()

    """ Searches for a stock value for a given company & date """

    def search(self, company, date):
        return self.companies_list[company].search(date)


setup = HashSetup()
setup.initialize_companies_map()

for i in range(5):
    date = input("Enter date in YYYYMMDD format: ")
    company = input("Enter company stock abbreviation: ")
    result = setup.search(company, date)
    print('%.2f' % result)
