import pandas
import os

class Expense:
    def __init__(self,description,amount):
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.description}, ${self.amount}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        if os.path.exists("Expense.csv"):
            self.pull_data_from_csv()
        else:
            pass

    def add_expense(self):
        get_expense = True
        while get_expense:
            category = input("Category: ").title()
            description = input("Description: ").title()
            amount = float(input("Amount: "))
            expense = Expense(description,amount)
            if category not in self.expenses:
                self.expenses[category] = []
            self.expenses[category].append(expense)
            print(f"Expense: {expense} added.")
            more_expense = input("Anymore expenses? 'y/n'").lower()
            if more_expense != "y":
                get_expense = False

    def check_expenses(self):
        if len(self.expenses) == 0 :
            print("There are no expenses. Add an expense.")
        else:
            for category,expense_list in self.expenses.items():
                print(category)
                for expense in expense_list:
                    print("=" * 20)
                    print(f"{expense}")
                    print("=" * 20)

    def total_expenses(self):
        total_expense = 0
        for category,expense_list in self.expenses.items():
            for expense in expense_list:
                total_expense += expense.amount
        print(f"Your total expenses are: ${total_expense}")

    def remove_expense(self):
        print("These are the categories")
        for category_index, category in enumerate(self.expenses):
            category_index += 1
            print("=" * 20)
            print(f"{category_index}: {category}")
            print("=" * 20)
        remove_category = input("Which category do you want to view? ").title()
 # maybe can add a full reset function
        for item_index, item in enumerate(self.expenses[remove_category]):
            item_index += 1
            print("These are the items")
            print("=" * 20)
            print(f"{item_index}: {item}")
            print("=" * 20)
        remove_item_index = int(input("Which index do you want to remove? "))
        confirmation = input(f"You have chosen to delete index no.{remove_item_index}. 'y/n' ").lower()
        remove_item_index -= 1
        if confirmation == "y":
            print(f"Item {self.expenses[remove_category][remove_item_index]} deleted.")
            del self.expenses[remove_category][remove_item_index]
            if len(self.expenses[remove_category]) == 0:
                del self.expenses[remove_category]

        else:
            pass

    def save_data_to_csv(self):
        """saving expenses to a CSV file"""
        expenses_dict = {}

        for category,expenses in self.expenses.items():
            expenses_dict[category] = []
            for expense in expenses:
                expense = str(expense)
                expenses_dict[category].append(expense)
        max_length = max(len(lists) for lists in expenses_dict.values())
        for category,expenses in self.expenses.items():
            if len(expenses_dict[category]) < max_length:
                amount_to_add = max_length - len(expenses_dict[category])
                counter = 0
                while counter != amount_to_add:
                    expenses_dict[category].append("")
                    counter += 1

        data = pandas.DataFrame.from_dict(expenses_dict)
        data.to_csv("Expense.csv")

    def pull_data_from_csv(self):
        data = pandas.read_csv("Expense.csv")
        data.drop(data.columns[0], axis=1, inplace=True)
        for category in data.columns:
            self.expenses[category] = []
            item_datas = data[category]
            for item in item_datas:
                if pandas.isna(item):
                    pass
                else:
                    item_split = item.split(",")
                    item_split1 = item_split[1].split("$")
                    expense = Expense(item_split[0], float(item_split1[1]))

                    self.expenses[category].append(expense)




