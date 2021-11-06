#allowance to create file paths across operating systems
import os
#import module for reading CSV Files and give path
import csv
budget_csvpath = os.path.join('Resources','budget_data.csv' )

#define variables for the process and lists to store data
months=[]
profits_losses = []
date=[]

total_months=0
total_profit_loss=0
priorprofit_loss=0
change=0
largest_increase=0
greatest_decrease=0


# use improved reading using the CSV Module
with open(budget_csvpath) as csvfile:
    # tell CSV reader the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header for the first row
    csv_header= next (csvreader)
   
    #Read rows after header and print them
    for row in csvreader:
        
        #count the months
        total_months += 1

        #calculate the total amount of profit/losses over the period
        total_profit_loss = total_profit_loss + int(row[1])

        #calculate the changes of profit/losses and find average of the changes
        #start by subtracting the profit or loss to the prior
        change= int(row[1]) - priorprofit_loss
        #add to a list of  profit or losses
        profits_losses.append(change)
        #replaces the profit loss to the prior 
        priorprofit_loss = int(row[1])
        average_change= (total_profit_loss/total_months)


        #Finding the largest inrease of profits and then the greatest decrease
        date.append(row[0])
        largest_increase=max(profits_losses)
        largest_date=date[profits_losses.index(largest_increase)]
        
        greatest_decrease=min(profits_losses)
        greatest_date=date[profits_losses.index(greatest_decrease)]
        

#print data to terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: $ {str(total_profit_loss)}")
print(f"Average Change: $ {str(round(change,2))}")
print(f"Greatest Increase in Profits: {largest_date} ($ {str(largest_increase)}")
print(f"Greatest Decrease in Profits: {greatest_date} ($ {str(greatest_decrease)}")


#export a text file with the results
with open('financial_analysis.txt', 'w') as text:

    text.write("Financial Analysis\n")
    text.write("------------------"+ "\n")
    text.write(f"Total Months: {str(total_months)}\n")
    text.write(f"Total: $ {str(total_profit_loss)}\n")
    text.write(f"Average Change: $ {str(round(change,2))}\n")
    text.write(f"Greatest Increase in Profits: {largest_date} ($ {str(largest_increase)}\n")
    text.write(f"Greatest Decrease in Profits: {greatest_date} ($ {str(greatest_decrease)}\n")