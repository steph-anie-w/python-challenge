# import & set path for csv file
import os
import csv

pybank_csv = os.path.join("..","PyBank","Resources","budget_data.csv")

# create lists to store data
#net_profit = []
changes_monthly = []
date = []

# set initial variable values
monthstotal = 0
total_profit = 0
net_change_profit = 0
initial_profit = 0

# open csv file and begin analysis
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile) 

    for row in csv.reader(csvfile):
        # sum months as progressing through csv file
        monthstotal = monthstotal + 1
        # store dates to find after calculating max/min values
        date.append(row[0])
        #net_profit.append(row[1])
        # begin collecting total profit information
        total_profit = total_profit + int(row[1])
        # calculate monthly change in profit
        profit = int(row[1])
        monthly_change_profit = profit - initial_profit
        changes_monthly.append(monthly_change_profit)
        #net_change_profit = net_change_profit + monthly_change_profit
        
        initial_profit = profit
        # calculate values utilizing existing variables & lists
        #average_change = ( / monthstotal)
        greatest_increase_amount = max(changes_monthly)
        greatest_decrease_amount = min(changes_monthly)
        greatest_increase_date = date[changes_monthly.index(greatest_increase_amount)]
        greatest_decrease_date = date[changes_monthly.index(greatest_decrease_amount)]

# print analysis in terminal
print("Financial Analysis")
print("-------------------------------------------")
print(f'Total Months: {int(monthstotal)}')
print(f'Total: ${total_profit}')
#print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})')

# export into text file