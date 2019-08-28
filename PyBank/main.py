import csv
import os

dates = []
pl = []

# Find the folder path of the executing python script to correctly locate the excel file no matter where it is
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'budget_data.csv')) as budget_data_file:
    budget_data = csv.DictReader(budget_data_file)
    # Iterate through each row in the excel data one by one and get the corresponding values for Date and Profit/Losses
    for row in budget_data:
        dates.append(row['Date'])
        pl.append(int(row['Profit/Losses']))

result = 'Financial Analysis\n---------------------------\n'

# Since each date includes unique month values, the number of months is equal to the length of dates list
result += 'Total Months: %d\n' % len(dates)

# Total profit is equal to the total values of the profit/losses (pl) list
result += 'Total: %d\n' % sum(pl)

# Calculate the changes in profit/losses from one month to another and save them in changes_in_pl list
changes_in_pl = []
for index in range(0, len(pl) - 1):
    changes_in_pl.append(pl[index + 1] - pl[index])

# The average change in pl is the sum of all changes divided by total number of changes
result += 'Average Change: %.2f\n' % (sum(changes_in_pl) / len(changes_in_pl))
# Note: a more effective but also more obscure calculation is (last profit - first profit) / number of changes
# C1 = X2 - X1, C2 = X3 - X2, ..., Cn-1 = Xn - Xn-1  ==> Ctotal = Xn - X1 ==> Cavg = Ctotal / n-1 = (Xn - X1) / (n - 1)
# result += 'Average Change: %.2f\n' % float((pl[-1] - pl[0]) / (len(pl) - 1))

# Find the maximum change in profit/loss, find its row index so that we can get its corresponding date from dates list
max_pl_change = max(changes_in_pl)
max_index = changes_in_pl.index(max_pl_change)
result += 'Greatest Increase in Profits: %s ($%d)\n' % (dates[max_index + 1], max_pl_change)

# Find the minimum change in profit/loss, find its row index so that we can get its corresponding date from dates list
min_pl_change = min(changes_in_pl)
min_index = changes_in_pl.index(min_pl_change)
result += 'Greatest Decrease in Profits: %s ($%d)\n' % (dates[min_index + 1], min_pl_change)

# Write results to the terminal
print(result)

# Write results to a text file
with open(os.path.join(__location__, 'result.txt'), 'w') as result_file:
    result_file.write(result)