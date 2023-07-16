import os
import csv

#csvpath = os.path.join('PyBank','Resources','budget_data.csv')
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

#month = []
#profit = []

with open(csvpath) as csvfile:    #, #newline=""

    csvreader = csv.reader(csvfile, delimiter=',')
