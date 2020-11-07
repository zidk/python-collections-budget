import csv
from datetime import datetime


class Expense:
    def __init__(self, date_str, vendor, category, amount):
        self.date_time = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        self.vendor = vendor
        self.category = category
        self.amount = amount


class Expenses:
    def __init__(self):
        self.list = []
        self.sum = 0

    # Read in the December spending data, row[2] is the $$, and need to format $$
    def read_expenses(self, filename):
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if '-' not in row[3]:
                    continue
                amount = float((row[3][2:]).replace(',', ''))
                self.list.append(Expense(row[0], row[1], row[2], amount))
                self.sum += amount

    def categorize_for_loop(self):
        necessary_expenses = set()
        food_expenses = set()
        unnecessary_expenses = set()
        for i in self.list:
            if (i.category == 'Phone' or i.category == 'Auto and Gas' or
                    i.category == 'Classes' or i.category == 'Utilities' or
                    i.category == 'Mortgage'):
                necessary_expenses.add(i)
            elif i.category == 'Groceries' or i.category == 'Eating Out':
                food_expenses.add(i)
            else:
                unnecessary_expenses.add(i)

        return [necessary_expenses, food_expenses, unnecessary_expenses]

    def categorize_set_compreshension(self):
        necessary_expenses = {
            x for x in self.list
            if
            x.category == 'Phone' or x.category == 'Auto and Gas' or x.category == 'Classes' or
            x.category == 'Utilities' or x.category == 'Mortgage'
        }
        food_expenses = {
            x for x in self.list
            if x.category == 'Groceries' or x.category == 'Eating Out'
        }
        unnecessary_expenses = set(self.list).difference(necessary_expenses).difference(food_expenses)

        return [necessary_expenses, food_expenses, unnecessary_expenses]

