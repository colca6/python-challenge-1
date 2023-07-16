import os
import csv

csvpath = os.path.join('PyBank','Resources','budget_data.csv')
#csvpath = os.path.join('PyPoll','Resources','election_data.csv')

#month = []
#profit = []

with open(csvpath) as csvfile:    #, #newline=""

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    firstrow = next(csvreader)
    #next(csvreader, None)
    #months = len(list(csvreader))
    #print(f"There are " + str(months) + " months in this file")
    total_months = 1
    #total = int(firstrow[1])
    previous_profit = int(firstrow[1])
    total_change = 0
    greatest_increase = int(firstrow[1])
    greatest_decrease = int(firstrow[1])
    months = 0
    #profit = 1
    profit = int(firstrow[1])
    
    for row in csvreader:
        
        total_months += 1
        profit += int(row[1])
        difference = int(row[1]) - previous_profit
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