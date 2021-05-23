#PyBank

import os
import csv

#Path to collect data from CSV file
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Define Variables
month_total = 0
net_revenue = 0
greatest_increase = 0
greatest_decrease = 0
increase_month = ""
decrease_month = "" 
monthly_change = 0
previous_month = 0
difference = 0


# Read the csv file
with open (budget_csv) as csv_file:

    #Split the data on commas
    csvreader = csv.reader(csv_file, delimiter=',')

    #Separate header
    header = next(csvreader)

        # Loop through the data
    for row in csvreader:

        #Count the number of months
        month_total = month_total + 1
        #print (month_total)

        # Find sum of P & L
        net_revenue = sum([int(row[1])])
        #print (net_pandl)

        # Calculate Average P&L monthly change
        avg_change = (net_revenue / month_total)
        #print(avg_change)


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