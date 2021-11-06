#allowance to create file paths across operating systems
import os
#import module for reading CSV Files and give path
import csv
poll_csvpath = os.path.join('Resources','election_data.csv' )

#define variables
#total number of votes for all candidates
total_votes=0
#a unique list of candidates
candidate_list_unique=[]
#number of votes per each candidate
number_of_votes =[]
#percentage of the votes per each candidate
percentage_of_votes = []

# use improved reading using the CSV Module
with open(poll_csvpath, newline="") as csvfile:
    # tell CSV reader the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #read the header for the first row
    csv_header= next (csvreader)
   
    #Read rows after header 
    for row in csvreader:
       #add a vote counter for total number of votes cast for all candidates
       total_votes= total_votes + 1
       
       #create a list for candidates names
       #if the candidate is on the list add candidate
       if row[2] not in candidate_list_unique:
           candidate_list_unique.append(row[2])
           index_candidate= candidate_list_unique.index(row[2])
           number_of_votes.append(1)
        #if candidate is on list add a vote
       else:
            index_candidate=candidate_list_unique.index(row[2])
            number_of_votes[index_candidate]+=1

    #add calucation for percentage of votes that each candidate won
    for votes in number_of_votes:
        #formula for percentage take individual votes per candidate and divde by total votes
        #then multiply by 100, and have it rounded as well
        percent=round((votes/total_votes)*100)
        percentage_of_votes.append(percent)

    #calualte the winner by looking at the max number of votes per the candidates
    winner=max(number_of_votes)
    winner_index= number_of_votes.index(winner)
    candidate_won= candidate_list_unique[winner_index]
   

#print outputs in terminal
print("Election Results")
print("------------------")
print(f"Total Votes: {total_votes}")
print("------------------")
for i in range(len(candidate_list_unique)):
    print(f"{candidate_list_unique[i]}: {percentage_of_votes[i]:.2f}% ({number_of_votes[i]})")
print("------------------")
print(f"Winner: {candidate_won}")
print("------------------")

#create a path for a Txt file
output_path = os.path.join('Analysis','Election_Results.txt')

#with the file open write Election Results
with open(output_path, 'w') as text:
    #print a text file
    text.write("Election Results\n")
    text.write("------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("------------------\n")
    for i in range(len(candidate_list_unique)):
        text.write(f"{candidate_list_unique[i]}: {percentage_of_votes[i]:.2f}% ({number_of_votes[i]})\n")
    text.write("------------------\n")
    text.write(f"Winner: {candidate_won}\n")
    text.write("------------------\n")