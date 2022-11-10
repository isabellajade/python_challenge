import os
import csv

csvpath = ".\\PyBank\\Resources\\budget_data.csv"

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    monthscount = 0
    totalprofit = 0
    previousprofit = 0
    currentprofit = 0
    changemonth = 0
    totalchange = 0
    greatestincrease = 0
    greatestincreasemonth = ""
    greatestdecrease = 0
    greatestdecreasemonth = ""

    for row in csvreader:
        monthscount += 1 
        totalprofit += int(row[1])
        currentprofit = int(row[1])
        change = 0

        if previousprofit != 0:
            change = currentprofit - previousprofit
            totalchange += change
            changemonth += 1

        previousprofit = currentprofit

        if change > greatestincrease:
            greatestincrease = change
            greatestincreasemonth = row[0]

        if change < greatestdecrease:
            greatestdecrease = change
            greatestdecreasemonth = row[0]

averagechange = totalchange / changemonth

output = f"""
Financial Analysis
----------------------------
Total Months: {monthscount}
Total: ${totalprofit:,}
Average Change: ${averagechange:,.2f}
Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease:,})
Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease:,})
""" 

print(output)

with open(".\\PyBank\\Analysis\\budget_analysis.txt", "w") as outputfile:
    outputfile.write(output)