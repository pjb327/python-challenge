import csv
import os
#what is os

PyBank_csv = os.path.join("Resources/budget_data.csv")


# The total number of months included in the dataset
date = []
profit = []

init_profit = 0
tot_profit = 0
count = 0
tot_change = []

with open(PyBank_csv, newline = "") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)

    for x in csv_reader:
        count = count + 1
        date.append(x[0])
        profit.append(int(x[1]))
    for y in profit:
        tot_profit = tot_profit + y
    for z in range(1, len(profit)):
        tot_change.append(int(profit[z]) - int(profit[z- 1]))
    inc_profit = max(tot_change)
    dec_profit = min(tot_change)
    max_date = date[tot_change.index(inc_profit) + 1]
    dec_date = date[tot_change.index(dec_profit) + 1]
    avg_change = sum(tot_change) / len(tot_change)
    print(f"Average change: {round(avg_change, 2)}")
    print(f"Increased profits: {max_date} {inc_profit}")
    print(f"Decreased profits: {dec_date} {dec_profit}")
    print(f"Total profits: {tot_profit}")
    print(f"Total months: {count}")







# The net total amount of "Profit/Losses" over the entire period


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


