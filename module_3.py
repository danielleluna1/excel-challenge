# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# csvpath = os.path.join('..', 'Resources', 'contacts.csv')
csvpath = "Resources/budget_data.csv"

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

print(csvpath)
total_months = 0
profit_losses = 0
total_change = 0
# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    print(csvreader)
    first_row = next(csvreader)
    
    p = int(first_row[1])
    total_months = 1
    profit_loss = p
   
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_months = total_months+1
        profit_losses = profit_losses+int(row[1])
        change = int(row[1]) - p
        total_change = total_change+change
        p = int(row[1])
print(total_months)
print(profit_losses)
print(total_change/(total_months-1))
# Caluculate profit/losses changes/average

