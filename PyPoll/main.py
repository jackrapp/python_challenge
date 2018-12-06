#election data columns: voter ID, county, candidate

import os
import csv

total = 0
winner= 0
candidate_list={}

#function for adding name and votes to dictionary
def sort_list(name):
    if name in candidate_list:
        #find vote count
        votes = candidate_list[str(name)]
        #increase vote count by 1
        candidate_list[str(name)] = votes + 1
    else:
        #if not found add to list
        candidate_list[(str(name))] = 1

#get data file
election_data = os.path.join("election_data.csv")

#read data file
with open(election_data, newline = "") as csvfile:
    votes = csv.reader(csvfile, delimiter = ",")
    next(votes)

    for row in votes:
        sort_list(row[2])
        total = total + 1

for name in candidate_list:
    winner = max(candidate_list[name], winner)
    if candidate_list[name] == winner:
        pywinner = name


#A complete list of candidates who received votes
print('''Election Results
----------------''')
print(f"Total Votes: {total}")
print("----------------")
for name in candidate_list:
    print(f"{name}: {'{:.2%}'.format(candidate_list[name]/total)} ({candidate_list[name]})")
print("----------------")
print(f"Winner: {pywinner}")
print("----------------")



#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.