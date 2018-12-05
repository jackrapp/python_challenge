#import modules
import csv
import os

budget_data = os.path.join("budget_data.csv")

profit = 0
months = 0
value = 0
increase = 0
decrease = 0

#pull data from csv file in git hub folder
with open(budget_data, newline="") as csvfile:
    records = csv.reader(csvfile, delimiter = ",")
    next(records)
    
#calculate
#total number of months in data
    for row in records:
        #monthly profit/loss
        value = int(row[1])
        #find number of months
        months = months + 1
        #total net profit/loss
        profit = profit + value
        #greatest increase in profits
        increase = max(increase, value)
        #greatest decrease in losses
        decrease = min(decrease, value)

    #total net profit/loss
    avg_monthly = int(profit)/int(months)

#print
print('''
Financial Analysis
------------------''')
print(f"Total Months: {months}")
print(f"Total: {profit}")
print(f"Average Change: {avg_monthly}")
print(f"Greatest Profit: {increase}")
print(f"Greatest Loss: {decrease}")

