import os
import csv

csvpath = os.path.join('PyBank','Resources','budget_data.csv')
#csvpath = os.path.join('PyPoll','Resources','election_data.csv')

with open(csvpath) as csvfile:    #, #newline=""

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    firstrow = next(csvreader)
    #Lots of variables to create to store values
    total_months = 1
    previous_profit = int(firstrow[1])
    total_change = 0
    greatest_increase = int(firstrow[1])
    greatest_decrease = int(firstrow[1])
    months = 0
    profit = int(firstrow[1])
    
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

        if difference > greatest_increase:
            greatest_increase = difference
            month_greatest_increase = row[0]
        elif difference < greatest_decrease:
            greatest_decrease = difference
            month_greatest_decrease = row[0]

        previous_profit = int(row[1])

    #average_change = total_change/total_months   
        #month.count(row[0])
        #profit.append(row[1])
        #profit.sort(reverse=True)

    #months = month.count(row[0])
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months : " + str(total_months))
    print("Total : " + str(profit))
    print("Average Change : " + str(average_change))
    print("Greatest Increase in Profits : " + str(month_greatest_increase + " (" + str(greatest_increase) + ")" ))
    print("Greatest Decrease in Profits : " + str(month_greatest_decrease + " (" + str(greatest_decrease) + ")" ))






"""     print(difference)
    print(total_change)
    print(greatest_increase)
    print(greatest_decrease)
    print(month_greatest_increase)
    print(month_greatest_decrease)
    print(greatest_decrease) """
       
    
    #print(f"CSV Header: {csv_header}")
    #print(csvreader)

    #for row in csvreader:
    #    print(row)
        
        #Task 1 of homework, number of months

    
    #netTotal = 0
    #for row in csvreader:
    #    netTotal += float(row[1])
    #print(netTotal)    