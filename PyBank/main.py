#PyBank

import os
import csv

#Path to collect data from CSV file
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Read the csv file
with open (budget_csv) as csv_file:

    #Split the data on commas
    csvreader = csv.reader(csv_file, delimiter=',')

    #Separate header
    header = next(csvreader)

        # Loop through the data
    num_months = 0
    for row in csvreader:

        #Count the number of months
        num_months = num_months + 1
        print (num_months)

        # Find sum of P & L
        net_pandl = sum([int(row[1])])
        #print (net_pandl)


#def profit_loss(budget_data)

    # Name Calculations
    # Total Months = sum(budget_data[0])
    # Net Profit/Loss


#Output Format
# print("Financial Analysis")
# print("-------------------------------------")
# print (f"Total Months: {month_total}")
# print (f"Total: ${net_total}")
# print (f"Average Change: ${avg_change}")
# print (f"Greatest Increase in Profits: {}")
# print (f"Greatest Decrease in Profits: {}")

# output_file=os.path.join("Resources", "financial_analysis.txt")