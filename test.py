import pandas
expenses = {}
data = pandas.read_csv("Expense.csv")
data.drop(data.columns[0], axis= 1, inplace= True)
for category in data.columns:
    expenses[category] = []
    item_datas = data[category]
    for item in item_datas:
        if pandas.isna(item):
            pass
        else:
            item_split = item.split(",")
            item_split1 = item_split[1].split("$")
            expense = (item_split[0],float(item_split1[1]))

            expenses[category].append(expense)
            print(expenses)




print(expenses)

test_string = "Sushi, $10.0"
parts = test_string.split(", ")
print(parts)