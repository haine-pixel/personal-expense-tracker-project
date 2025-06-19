from ExpenseTracker import ExpenseTracker
tracker = ExpenseTracker()

print("=" * 20)
print("1. Add Expense")
print("2. Check Expense")
print("3. Check total Expenses")
print("4. Remove Expense")
print("5. Exit")
print("=" * 20)
tracker_on = True
while tracker_on:
    choice = int(input("Choose an option: "))
    if choice == 1:
        tracker.add_expense()
    elif choice == 2:
        tracker.check_expenses()
        #the category is showing even when there is no item in it. see if it can print: no expenses
        #if there is not item in any category
    elif choice == 3:
        tracker.total_expenses()
        # total expense not working, see if I can get it to work
    elif choice == 4:
        tracker.remove_expense()
        #make it remove the category as well once there is nothing in the category
    elif choice == 5:
        break
    else:
        print("Invalid choice.")