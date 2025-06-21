from ExpenseTracker import ExpenseTracker
tracker = ExpenseTracker()


tracker_on = True
while tracker_on:
    print("=" * 20)
    print("1. Add Expense")
    print("2. Check Expense")
    print("3. Check total Expenses")
    print("4. Remove Expense")
    print("5. Exit")
    print("=" * 20)
    choice = int(input("Choose an option: "))
    if choice == 1:
        tracker.add_expense()
    elif choice == 2:
        tracker.check_expenses()
    elif choice == 3:
        tracker.total_expenses()
    elif choice == 4:
        tracker.remove_expense()
    elif choice == 5:
        tracker.save_data_to_csv()
        break
    else:
        print("Invalid choice.")