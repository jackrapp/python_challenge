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
        if increase == value:
            inc_month = row[0]
        #greatest decrease in losses
        decrease = min(decrease, value)
        if decrease == value:
            dec_month = row[0]

    #total net profit/loss
    avg_monthly = int(profit)/int(months)

print("Financial Analysis")
print("------------------")
print(f"Total Months: {months}")
print(f"Total: {profit}")
print(f"Average Change: {avg_monthly}")
print(f"Greatest Profit: {inc_month} ({increase})")
print(f"Greatest Loss: {dec_month} ({decrease})") 

#print out results and send as text file
with open("pybank_analysis.txt", "w") as pybank_analysis:
    print("Financial Analysis", file = pybank_analysis)
    print("------------------", file = pybank_analysis)
    print(f"Total Months: {months}", file = pybank_analysis)
    print(f"Total: {profit}", file = pybank_analysis)
    print(f"Average Change: {avg_monthly}", file = pybank_analysis)
    print(f"Greatest Profit: {inc_month} ({increase})", file = pybank_analysis)
    print(f"Greatest Loss: {dec_month} ({decrease})",file = pybank_analysis)    

