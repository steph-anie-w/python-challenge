# import & set path for csv file
import os
import csv

pybank_csv = os.path.join("..","PyBank","Resources","budget_data.csv")

# create lists and variables
changes_monthly = []
date = []
monthstotal = 0
total_profit = 0
initial_profit = 0

# open csv file and begin analysis
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile) 
    for row in csv.reader(csvfile):

# count total number of months in data
        monthstotal = monthstotal + 1

 # net Profit/Losses over entire period
        total_profit = total_profit + int(row[1])

# calculate monthly change in profit and average
        profit = int(row[1])
        monthly_change_profit = profit - initial_profit
        changes_monthly.append(monthly_change_profit)
        average_change = round((sum(changes_monthly) / monthstotal), 2)
        initial_profit = profit

# greatest increase and decrease in Profit/Losses (date & amount)
        date.append(row[0])
        greatest_increase_amount = max(changes_monthly)
        greatest_decrease_amount = min(changes_monthly)
        greatest_increase_date = date[changes_monthly.index(greatest_increase_amount)]
        greatest_decrease_date = date[changes_monthly.index(greatest_decrease_amount)]

# print analysis in terminal
print("Financial Analysis")
print("-------------------------------------------")
print(f'Total Months: {int(monthstotal)}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})')

# export into text file
output_file = os.path.join("..", "PyBank", "Analysis", "PyBank_Analysis.csv")
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------------------------"])
    csvwriter.writerow([f'Total Months: {int(monthstotal)}'])
    csvwriter.writerow([f'Total: ${total_profit}'])
    csvwriter.writerow([f'Average Change: ${average_change}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})'])