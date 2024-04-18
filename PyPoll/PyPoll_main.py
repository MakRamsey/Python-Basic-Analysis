#Please note: This code was worked on with collaboration with academic tutors and classmates
#First import the necessary modules to execute this code
#os for file path simplicity & csv for reading CSV files

import os
import csv

#assign variable to hold path/address to CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

#open and read the CSV file by initiating a with loop that while open, variable csvreader is going to hold the readable version of the csv file
with open(csvpath) as opening:
    #utilizing the reader function imported via the csv module, we are reading the 'csvfile' (variable holding the opened path) and storing the value in csvreader
    csvreader = csv.reader(opening, delimiter=",")
    #Skipping the header row of the data to exclude column titles (stored for potential callback later)
    header = next(csvreader, None)
    
    #Set variable "candidate" to hold a dictionary with keys = "candidate name" and value = "candidate's votes
    candidate = {}

    #initiate for loop that cycles through each row within the readable csv file providing a mechanism to derive insights from the data
    #this loop will keep track of each row/vote and attribute that vote to the correct candidate based on their respective names
    for row in csvreader:
        name = row[2]
        if name in candidate:
            current_votes = candidate[name]
            current_votes += 1
            candidate[name] = current_votes
        else:
            candidate[name] = 1

    #print(candidate) for confirmation of correct values within dictionary

    #determine total votes by adding all the values within our dictionary
    total_votes = candidate["Charles Casper Stockham"] + candidate["Diana DeGette"] + candidate["Raymon Anthony Doane"]
    #print(total_votes)

    #determine each candidate's respective vote percentage, store in a variable and round according to proper formatting
    candidate_one_pct = round((candidate["Charles Casper Stockham"] / total_votes) * 100, 3)
    candidate_two_pct = round((candidate["Diana DeGette"] / total_votes) * 100, 3)
    candidate_three_pct = round((candidate["Raymon Anthony Doane"] / total_votes) * 100, 3)


    #initiate a list to hold the found percent values to zip with dictionary below for final print
    pct_list = [candidate_one_pct, candidate_two_pct, candidate_three_pct]
    #print(pct_list) for confirmation

    #assign variables for unique string values that represent each candidate within the election
    candidate_one = "Charles Casper Stockham"
    candidate_two = "Diana DeGette"
    candidate_three = "Raymon Anthony Doane"

    #initiate if/and statements to determine winner
    if candidate_one_pct > candidate_two_pct and candidate_one_pct > candidate_three_pct:
        winner = candidate_one
    elif candidate_two_pct > candidate_one_pct and candidate_two_pct > candidate_three_pct:
        winner = candidate_two
    elif candidate_three_pct > candidate_one_pct and candidate_three > candidate_two_pct:
        winner = candidate_three

    #print results according to proper/desired format
    print("Election Results")
    print("                ")
    print('------------------------------')
    print("                ")
    print(f"Total Votes: {total_votes}")
    print("                ")
    print('------------------------------')
    print("                ")
    for (key, value), pct in zip(candidate.items(), pct_list):
        print(f'{key}: {pct}% ({value})')
        print("                ")
    print('------------------------------')
    print("                ")
    print(f'Winner: {winner}')
    print("                ")
    print('------------------------------')

#create string variable to hold program results for future export
output = '''
Election Results
                
------------------------------
                
Total Votes: 369711
                
------------------------------
                
Charles Casper Stockham: 23.049% (85213)
                
Diana DeGette: 73.812% (272892)
                
Raymon Anthony Doane: 3.139% (11606)
                
------------------------------
                
Winner: Diana DeGette
                
------------------------------'''

#print(output)

#assign variable to hold output path for analysis text file
output_path = os.path.join('Analysis', "Py_Poll_Analysis.txt")

#export results to separate text file within out "Analysis" folder
with open(output_path, 'w') as output_file:
    print(output, file=output_file)
