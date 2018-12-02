#import modules
import csv
import os

budget_data = os.path.join("budget_data.csv")

profit = 0
increase = 0
decrease = 0

#pull data from csv file in git hub folder
with open(budget_data, newline="") as csvfile:
    records = csv.reader(csvfile, delimiter = ",")
    next(records, None)
    
#calculate
#total number of months in data
    for row in records:
        #total number of months in data
        months = len(list(records))
        #total net profit/loss
        profit =+ int(row[1])
        #average mothly change
        avg_monthly = int(profit)/int(months)
        #greatest increase in profits
        if int(row[1]) > increase:
            increase == int(row[1])
        #greatest decrease in losses
        elif int(row[1]) < decrease:
            decrease == int(row[1])

#print
print('''
Financial Analysis
------------------''')
print(f"Total Months: {months}")
        #Total: {profit}
        #Average Change: {avg_monthly}
        #Greatest Profit: {increase}
        #Greatest Loss: {decrease}

