#PyBank

import os
import csv

#Path to collect data from CSV file
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Define Variables
month_total = 0
net_rev = 0
greatest_increase = 0
greatest_decrease = 0
increase_month = ""
decrease_month = "" 
current_rev = 0
previous_rev = 0
monthly_change = 0
difference = 0
change = []


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
        
        # Calculate net revenue
        net_rev = float(net_rev) + float(row[1])

        # Calculate monthly profit change
        if (month_total == 1):
            previous_rev = int(row[1])

        else:
            current_rev = int(row[1])
            previous_rev = int(row[1])
            monthly_change = current_rev - previous_rev
            change.append(monthly_change)
            

        # Find sum of P & L
        # print (net_pandl)

# Calculate Average change
avg_change = sum(change) / len(change)
        #print(avg_change)


#Output Format
print("Financial Analysis")
print("-------------------------------------")
print (f"Total Months: {month_total}")
print (f"Total: ${round(net_rev)}")
print (f"Average Change: ${avg_change}")
# print (f"Greatest Increase in Profits: {}")
# print (f"Greatest Decrease in Profits: {}")

# output_file=os.path.join("Resources", "financial_analysis.txt")