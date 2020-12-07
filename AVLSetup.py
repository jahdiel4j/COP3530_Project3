import csv
from AVLTree import AVLTree
import time

class AVLSetup:
    # Dictionary/Map of Company AVL Trees
    companies_list = {}
    # List of companies in order of the CSV file's columns
    ordered_companies = []
    # Elapsed time to insert all nodes into AVL
    setup_time = 0

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

        s = time.time_ns()

        for i in range(len(companies)):
            # Index 0 in the 1st row is where it says "Date"
            if i != 0:
                self.companies_list[companies[i]] = AVLTree()
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

        e = time.time_ns()
        self.setup_time = e-s
        csv_file.close()

    """ Searches for a stock value for a given company & date """
    def search(self, company, date):
        date = self.convert_date(date)
        # compute and return value of given company at given date
        return self.companies_list[company].search(date)

    def find_best_stock_growth(self, companies, start_date, end_date):
        max_growth = -10000 # arbitrary value to compare initial growth. No stock drops $10000 in one day, so we are safe
        max_company = ""   # if all the companies are invalid at the given dates, say holiday, returns empty string for company name

        start_date = self.convert_date(start_date)
        end_date = self.convert_date(end_date)

        # for every company the user wanted to compare
        for company in companies:
            # compute value of company at start and end dates
            start_value = self.companies_list[company].search(start_date)
            end_value = self.companies_list[company].search(end_date)

            # if the company value was valid at both dates and the growth is greater than the maximum growth,
            # reassign return values to current company
            if start_value != -1 and end_value != -1 and end_value-start_value > max_growth:
                max_growth = (end_value-start_value)
                max_company = company

        return max_company, max_growth

    def find_worst_stock_growth(self, companies, start_date, end_date):
        min_growth = 10000  # arbitrary value to compare initial growth. No stock grows $10000 in one day, so we are safe
        min_company = ""   # if all the companies are invalid at the given dates, say holiday, returns empty string for company name

        start_date = self.convert_date(start_date)
        end_date = self.convert_date(end_date)

        # for every company the user wanted to compare
        for company in companies:
            # compute value of company at start and end dates
            start_value = self.companies_list[company].search(start_date)
            end_value = self.companies_list[company].search(end_date)

            # if the company value was valid at both dates and the growth is less than the minimum growth,
            # reassign return values to current company
            if start_value != -1 and end_value != -1 and end_value-start_value < min_growth:
                min_growth = (end_value-start_value)
                min_company = company

        return min_company, min_growth
