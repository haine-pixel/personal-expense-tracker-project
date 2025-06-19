class Expense:
    def __init__(self,description,amount):
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.description}, {self.amount}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

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

            print(f"{expense}")

            more_expense = input("Anymore expenses? 'y/n'").lower()
            if more_expense != "y":
                get_expense = False

    def check_expenses(self):
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
        return total_expense

    def check_total(self):
        total = self.total_expenses()
        print(f"{total}")

    def remove_expense(self):
        print("These are the categories")
        for category_index, category in enumerate(self.expenses):
            category_index += 1
            print("=" * 20)
            print(f"{category_index}: {category}")
            print("=" * 20)
        remove_category = input("Which category do you want to view? ").title()
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

        else:
            pass

