# Import Dependencies
import os
import csv


py_bank_path = os.path.join('.', 'Resources', 'budget_data.csv')

# Open and read csv file
with open(py_bank_path) as py_bank_data:
    budget_reader = csv.reader(py_bank_data, delimiter=',')

    # Skip the header
    csv.header = next(budget_reader)

    # Read "Profit/Losses" from file and save to separate list
    month_list = []
    budget_list = []
    for budget in budget_reader:
        month_list.append(budget[0])
        budget_list.append(float(budget[1]))

# Save the changes to separate list
change_list = []
for i in range(len(budget_list) - 1):
    f = budget_list[i + 1] - budget_list[i]
    change_list.append(f)

# Find Total Months
total_months = len(budget_list)

# Find Total
total = sum(budget_list)

# Find Average  Change
average_change = (sum(change_list) / len(change_list))

# Find Greatest Increase in Profits
max_profit = max(change_list)

# Find the month for Greatest Increase in Profits
max_month_profit = month_list[change_list.index(max_profit)+1]

# Find Greatest Decrease in Profits
min_profit = min(change_list)

# Find the mont Greatest Decrease in Profits
min_month_profit = month_list[change_list.index(min_profit)+1]


# Export the results to a text file
with open("ResultBank.txt", "w") as pyBank_result:
    pyBank_result.write("Financial Analysis" + "\n")
    pyBank_result.write("-" * 20 + "\n")
    pyBank_result.write("Total months: {0}".format(str(total_months)) + "\n")
    pyBank_result.write("Total: ${0}".format(str(round(total))) + "\n")
    pyBank_result.write("Average change: ${0}".format(str(round(average_change, 2))) + "\n")
    pyBank_result.write("Greatest Increase in Profits: {0} (${1})".format(max_month_profit, str(round(max_profit))) + "\n")
    pyBank_result.write("Greatest Decrease in Profits: {0} (${1})".format(min_month_profit, str(round(min_profit))) + "\n")

#  Print the analysis to the terminal
print("Financial Analysis")
print("-" * 20)
print("Total months: {0}".format(str(total_months)))
print("Total: ${0}".format(str(round(total))))
print("Average change: ${0}".format(str(round(average_change,2))))
print("Greatest Increase in Profits: {0} (${1})".format(max_month_profit,str(round(max_profit))))
print("Greatest Decrease in Profits: {0} (${1})".format(min_month_profit,str(round(min_profit))))
