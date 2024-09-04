# Import the necessary modules: os for file path simplicity & csv for reading CSV files

import os
import csv

# assign variable to hold path/address to CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# open and read the CSV file by initiating a with loop that while open, variable csvreader is going to hold the readable version of the csv file
with open(csvpath) as csvfile:

    # utilizing the reader function imported via the csv module, we are reading the 'csvfile' (variable holding the opened path) and storing the value in csvreader
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skipping the header row of the data to exclude column titles (stored for potential call back later)
    header = next(csvreader, None)

    # Set variables in order to track desired results
    month_list = []
    net_start = 0
    last_rev = None
    change_list = []

    # initiate for loop that cycles through each row within the readable csv file providing a mechanism to derive insights from the data
    for rows in csvreader:

        # adding or "appending" each row to a callback list which can be len"ed" to obtain the total number of months
        month_list.append(rows)

        # because net_start variable was previously defined as zero, we can iterate it with the corresponding integer value from each rows to obtain a total count
        net_start += int(rows[1])

        # initiate profit_or_loss variable that will enter into the below if loop (for the second row once last_rev resets with a value
        # this will serve as a relative starting point for revenue change calculations
        profit_or_loss = int(rows[1])

        if last_rev is not None:

            # on second pass this if loop is entered which calculates the delta between each entries revenue numbers
            delta = profit_or_loss - last_rev

            # adding or "appending each delta to the change_list initiated above
            change_list.append(delta)

        last_rev = profit_or_loss

    # open a dictionary in order to combine gathered data in order to later oput the greatest increase/decrease numbers along with their respective dates
    Date_PL = {}

    # resetting the csv file in ordre to allow it to be "re-read"
    csvfile.seek(0)

    # must initiate another variable to hold the second "read" of the file once reset from above
    csvreader2 = csv.reader(csvfile, delimiter=',')

    # Skipping the header row of the data to exclude column titles
    next(csvreader2, None)

    # initiate second for loop that cycles through each row within the readable csv file (version 2) providing a mechanism to derive insights from the data
    for rows in csvreader2:

        # storing the key-value pairs as "DATE":int(REVENUE) within our dictionary
        Date_PL[rows[0]] = int(rows[1])

    # define max and min change within out delta or change list representing the net change from day to day
    max_change = max(change_list)
    min_change = min(change_list)

    # define two variables to hold the string values of the months when the greatest increase/deacrease occurred
    month_increase = ""
    month_decrease = ""

    # initiate another for loop to cycle through each row, adding the change list value to the corresponding entry and identifying if it was max or min
    for i, rows in enumerate(Date_PL.items()):
        if i != 0:
            Date_PL[rows[0]] = change_list[i - 1]
            if change_list[i - 1] == max_change:
                month_increase = rows[0]
            if change_list[i -1] == min_change:
                month_decrease = rows[0]

    # calculating average change between each row's revenue by using our change_list
    average_change = sum(change_list) / len(change_list)

    # establishing month count varaible to hold/represent the length of the month list previously derived
    month_count = len(month_list)

    # printing full analysis according to requested formatting
    print("Financial Analysis")
    print("---------------------------")
    print(f'Total Months: {month_count}')
    print(f'Total: ${net_start}')
    print(f'Average Change: ${round(average_change, 2)}')
    print(f'Greatest Increase in Profits: {month_increase} (${max(Date_PL.values())})')
    print(f'Greatest Decrease in Profits: {month_decrease} (${min(Date_PL.values())})')

# create string variable to hold program results for future export
output = '''
Financial Analysis
---------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)'''

# assign variable to hold output path for analysis text file
output_path = os.path.join('Analysis', "Py_Bank_Analysis.txt")

# export results to separate text file within out "Analysis" folder
with open(output_path, 'w') as output_file:
    print(output, file=output_file)