import os
import csv

# create variables for storing information
vote_count = [] # find the length to get the number of votes cast
candidate_names = [] # attributes the name for each vote, this is going to generate duplicates of each name which we'll sort later.
candidate_count = [] # the count each candidate received.

csv_election = os.path.join('Resources', 'election_data.csv')

with open(csv_election) as csv_file:
        
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    #skip the first row because it's just the row titles
    csv_header = next(csv_file)
    
    for row in csv_reader:
        
        # append the empty list to add ALL the ballot ID numbers to it. Find the length to get the amount of ballots cast.
        vote_count.append(row[0])
        
        # append the names list to all the votes for all candidates.
        candidate_names.append(row[2])
        
    # This generates populates a list (candidate_names_w_vote) of each of the unique elemets in the list (candidate_names).
    candidate_list_w_vote = list(set(candidate_names))
        
    # This command runs through each candidate in the list (candidate_list_w_vote) and appends the (candidate_count) to count how many times each candidate appears in (candidate_names)
    # i.e how many votes they received
    for i in candidate_list_w_vote:
        
        # Has to be an integer to use in calculations for the output
        candidate_count.append(int(f'{candidate_names.count(i)}'))
        
# We create a summary table by zipping together each name and the count in the data. For use in calculations later.
candidate_summary = list(zip(candidate_list_w_vote, candidate_count))  
             
print("======================================================================================")
print("")
print("ELECTION RESULTS")
print("")
print("======================================================================================")
print("")
print("The total number of votes cast was:")        
print(len(vote_count))
print("")
print("======================================================================================")
print("")

# Cycles through each row in the summary and concatenates the name, vote percent, and vote tally of each candidate.
for row in candidate_summary:
    
    vote_percent = round(row[1] / sum(candidate_count) * 100, 3)
    
    print(row[0] + " received " + str(vote_percent) + "%" + " of the votes." + " " + str(row[1]) )

print("")
print("======================================================================================")
print("")

# Checks the vote count in row 2 of the the summary table. If it is equal to the max count we print the winner (row 1) of the summary table/.
for i in candidate_summary:
    
    if i[1] == max(candidate_count):
        print("Winner: " + f'{i[0]}')
        
print("")
print("======================================================================================")


# Write information to .txt

file_path = "analysis/PyPoll_analysis.txt"

file = open(file_path, 'w')

# Use \n to write each piece of information on a new line
file.write("\n" + "======================================================================================")
file.write("\n" + "ELECTION RESULTS")
file.write("\n" + "======================================================================================")

file.write("\n" + "")
file.write("\n" + "The total number of votes cast was:")
file.write("\n" + "")
file.write("\n" + str(len(vote_count)))
file.write("\n" + "")
file.write("\n" +"======================================================================================")
file.write("\n" + "")

for row in candidate_summary:
    
    file.write("\n" + row[0] + " received " + str(vote_percent) + "%" + " of the votes." + " " + str(row[1]))
    file.write("\n" + "")

file.write("\n" +"======================================================================================")
file.write("\n" + "")    

for i in candidate_summary:
    
    if i[1] == max(candidate_count):
        file.write("\n" + "Winner: " + f'{i[0]}' )
    
file.write("\n" + "")
file.write("\n" +"======================================================================================")



file.close() 