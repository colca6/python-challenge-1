#set up environment
import os
import csv

#create relative path to file to read
csvpath = os.path.join('Resources','budget_data.csv')

#open file with reader object
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #save header info here:
    csv_header = next(csvreader)
    #save value in the first row so when we iterate, we have a starting value to compare new row data to.
    firstrow = next(csvreader)

    #Lots of variables to create to store values
    total_months = 1
    previous_profit = int(firstrow[1])
    total_change = 0
    greatest_increase = int(firstrow[1])
    greatest_decrease = int(firstrow[1])
    months = 0
    profit = int(firstrow[1])
    
    #loop through data
    for row in csvreader:
        #get total numbr of months
        total_months += 1
        #As we loop through the recordset, add rows profit/loss to profit variable (add to running total)
        profit += int(row[1])
        #need to calculate difference from month to month. loop keeps previous month's value in "previous_profit",
        #so here you can subtract current month with previous month, the "difference" will be
        #the increase or decrease
        difference = int(row[1]) - previous_profit
        #Total change is from beginning to end, so add to running total, the difference value. Same with 
        #average change, it grows, but when the for loop finishes, these variables will hold the final values.
        total_change += difference
        average_change = total_change/(total_months -1)

        #Double whammy-do math to check for numerical increase/decrease while also holding the associated month
        if difference > greatest_increase:
            greatest_increase = difference
            month_greatest_increase = row[0]
        elif difference < greatest_decrease:
            greatest_decrease = difference
            month_greatest_decrease = row[0]
        #reset "previous_profit" to that row's data so we can compare new month to it
        previous_profit = int(row[1])

    #Print to terminal
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months : " + str(total_months))
    print("Total : " + str(profit))
    print("Average Change : " + str(round(average_change,2)))    #round to two decimal points
    print("Greatest Increase in Profits : " + str(month_greatest_increase + " (" + str(greatest_increase) + ")" ))
    print("Greatest Decrease in Profits : " + str(month_greatest_decrease + " (" + str(greatest_decrease) + ")" ))

    #Write out to text file instructions
    #Note position of indentation.
outpath = os.path.join('Analysis','analysis_results.txt')

#open text file to write into. Call .write().    '\n' makes line break, else would all be one line.
#Also 'w' inside () indicates write to it.
with open(outpath, 'w') as file:
    file.write("Financial Analysis" + '\n')
    file.write("-----------------------------" + '\n')
    file.write("Total Months : " + str(total_months) + '\n')
    file.write("Total : " + str(profit) + '\n')
    file.write("Average Change : " + str(round(average_change,2)) + '\n')
    file.write("Greatest Increase in Profits : " + str(month_greatest_increase + " (" + str(greatest_increase) + ")" ) + '\n')
    file.write("Greatest Decrease in Profits : " + str(month_greatest_decrease + " (" + str(greatest_decrease) + ")" ))
 