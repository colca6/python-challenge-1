#set up environment
import os
import csv

#csvpath = os.path.join('PyBank','Resources','budget_data.csv')
csvpath = os.path.join('Resources','election_data.csv')

#List for holding Candidate names
list_candidates = []
#Dictonary for holding candidate names and vote totals
dict_candidates = {}

#Use the relative path to open the appropriate file into a csv.reader object
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #save column headers
    csv_header = next(csvreader)
    

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

    #for loop has now ended
    #This returns the total votes by summing the (3) values in dict_candidates.
    votes_per_cand = sum(dict_candidates.values())
    #This returns the maximum value in dictionary in order to determine who won.
    winning_num = max(dict_candidates.values())
    #Use a list comprehension to return the key for winning_num variable.
    winner = {cand for cand in dict_candidates if dict_candidates[cand] == winning_num}
    
    #Print to terminal instructions
    print("Election Results")
    print("------------------------------------------")
    print(f"Total Votes:  {votes_per_cand}")
    print("------------------------------------------")
    #The following loop uses the dictionary items() function to print the 3 candidates' info
    for key, value in dict_candidates.items():
        #"key" is candidate name, "value" is count of votes, round function to limit decimal places
        print(key,": ", round((int(value)/int(votes_per_cand))*100,3),"% (", value, ")")

    print("------------------------------------------")
    #Annoyingly, dictionary fields print funny, with curly brackets, in this case also single quotes which might be due
    #to casting as string. In any case, replace function works.
    print(f"Winner:  {str(winner)}".replace("{'","").replace("'}",""))
    print("------------------------------------------")


    #Write out to text file instructions
    #Note position of indentation. Also 'w' inside () indicates open file to write to it.
#with open('analysis_results.txt', 'w') as file:
outpath = os.path.join('Analysis','analysis_results.txt')


#open text file to write into
with open(outpath, 'w') as file:


    #call write function.  '\n' makes it go to new line.
    file.write("Election Results" + '\n')
    file.write("------------------------------------------" + '\n')
    file.write(f"Total Votes:  {votes_per_cand}" + '\n')
    file.write("------------------------------------------" + '\n')
    #The following loop uses the dictionary items() function to print the 3 candidates' info
    for key, value in dict_candidates.items():
        #"key" is candidate name, "value" is count of votes, round function to limit decimal places
        file.write(str(key) + " : " + str(round((int(value)/int(votes_per_cand))*100,3)) + "% ( " +  str(value) + ")" + '\n')
        
    file.write("------------------------------------------" + '\n')
    #Annoyingly, dictionary fields print funny, with curly brackets, in this case also single quotes which might be due
    #to casting as string. In any case, replace function works.
    file.write(f"Winner:  {str(winner)}".replace("{'","").replace("'}","") + '\n')
    file.write("------------------------------------------")
