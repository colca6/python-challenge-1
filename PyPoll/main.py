import os
import csv

#csvpath = os.path.join('PyBank','Resources','budget_data.csv')
csvpath = os.path.join('PyPoll','Resources','election_data.csv')


#List for holding Candidate names
list_candidates = []
#Dictonary for holding candidate names and vote totals
dict_candidates = {}

#Use the relative path to open the appropriate file into a csv.reader object
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #firstrow = next(csvreader)

    #the csv file has 3 columns, Ballot ID, county, candidate. For this exercise, we only want the
    #candidate names, and since each row (1 row per ballot ID) represents 1 vote, number of rows per name.
    #Therefore, we can loop through records using the only the Candidate col of the csv.
    #First we set variable name = the candidate name in the row, then we will append it to a list, 
    #IF AND ONLY IF it's not already in the list. A "select(distinct(name))" if you will.
    for row in csvreader:
        name = (row[2])

        #List "list_candidates" is an empty list object. Easiest way, for me, rather than comparing 
        #each row in the recordset to the previous row, is just to say "if it's not already in there, add it".
        #by using NOT.  I tried to use "set" but that turned out to be confusing.
        if name not in list_candidates:
            list_candidates.append(name)

            #Since list can only hold a single list of items, and we want associated data, use dictionary.
            #dict_candidates is our empty dictionary that will hold key (candidate) and values.
            #In this case we want to count the rows (each row = 1 vote) per candidate.
            #If we use Candidate name as the key, these have to be unique, so will create only one key:value
            #per candidate. By using an integer for the value and adding 1 for each record in csv file, 
            #the value for each candidate continues to grow until the name (key) changes, thus becoming 
            #a counter.
            #loop starts with first name and value adds 1 for each row. Note that it's set to 0
            #inside the if statement, so that at the beginning and for each NEW candidate, the "counter"
            #resets to zero.  If candidate is already in list, the if statement is exited (note the
            #change in indentation), and "1" is added to the value.
            dict_candidates[name] = 0 
        dict_candidates[name] += 1
        #The dict_candidates dictionary:
        # {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}
        #-----------------------------

    #This returns the total votes by summing the values in dict_candidates.
    #votes_per_cand = dict_candidates.values()
    votes_per_cand = sum(dict_candidates.values())
    #This returns the maximum value in vote_dict. This is used to declare a winner.
    winning_num = max(dict_candidates.values())
    #Use a list comprehension to return the key for winning_num variable.
    winner = {i for i in dict_candidates if dict_candidates[i] == winning_num}
    
    #Print to terminal instructions
    print("Election Results")
    print("------------------------------------------")
    print(f"Total Votes:  {votes_per_cand}")
    print("------------------------------------------")
    #The following loop uses the dictionary items() function
    for key, value in dict_candidates.items():
        
        print(key,": ", round((int(value)/int(votes_per_cand))*100,3),"% (", value, ")")

    print("------------------------------------------")
    #Annoyingly, dictionary fields print funny, with curly brackets, in this case also single quotes which might be due
    #to casting as string. In any case, replace function works.
    print(f"Winner:  {str(winner)}".replace("{'","").replace("'}",""))
    print("------------------------------------------")
    #print(dict_candidates)


"""     for row in csvreader:
        
        total_votes += 1
        name.append(row[2])
        #Create set to get unique values
        
    for x in set(name):
        candidate.append(x)
        y = name.count(x)
        #print(name)
        vote_per_cand.append(y)

        z = (y/total_votes)*100
        percentage.append(z)


    most_votes = max(vote_per_cand)
    winner = candidate[vote_per_cand.index(most_votes)] """


""" print("Total Votes :" + str(total_votes))
print("-------------------------")
for i in range(len(name)):
            print(name[i] + ": " + str(round(percentage[i])) +"% (" + str(vote_per_cand[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------") """




"""         curr_cand = str(row[2])
        if curr_cand != candidate:
            distinct_cand.append(curr_cand) """

        

"""         if difference > greatest_increase:
            greatest_increase = difference
            month_greatest_increase = row[0]
        elif difference < greatest_decrease:
            greatest_decrease = difference
            month_greatest_decrease = row[0] """



""" print(total_votes)
print(curr_cand)
print(candidate) """
#print(distinct_cand)

"""         def get_distinct_cand(csvreader):
            distinct_cand = []
            if candidate in csvreader:
                continue
            else:
                distinct_cand.append(str(row[2]))
            return distinct_cand """
    



    #print(distinct_cand)

        #total = int(firstrow[1])
    #previous_profit = int(firstrow[1])
    #total_change = 0
    #greatest_increase = int(firstrow[1])
    #greatest_decrease = int(firstrow[1])
    #months = 0
    #profit = 1
    #profit = int(firstrow[1])


"""         total_votes = 1
    candidate = str(firstrow[2])
    most_votes = int(firstrow[0])
    
    distinct_cand = []
    for candy in candidate:
        distinct_cand.append(candy)
    curr_cand = str(firstrow[2]) """