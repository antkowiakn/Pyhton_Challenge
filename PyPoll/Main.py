#allowance to create file paths across operating systems
import os
#import module for reading CSV Files and give path
import csv
poll_csvpath = os.path.join('Resources','election_data.csv' )

#define variables
total_votes=0
candidate_list=[]
number_of_votes =[]
percentage_of_votes = []

with open(poll_csvpath, newline="") as csvfile:
    # tell CSV reader the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header for the first row
    csv_header= next (csvreader)
   
    #Read rows after header and print them
    for row in csvreader:
       #add a vote counter for total number of votes cast
        total_votes= total_votes +1

#print outputs in terminal
print("Election Results")
print("------------------")
print(f"Total Votes: {total_votes}")
print("------------------")
