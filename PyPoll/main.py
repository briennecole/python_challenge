import csv
import collections as ct
import os

# Path to csv file
votes = os.path.join('Resources', 'election_data.csv')


#define variables
vote_total = 0
vote_percent = float
winner = ""
max_vote = 0

# loop through to count votes
# https://stackoverflow.com/questions/52286104/count-number-of-times-a-candidate-has-been-voted-for
with open(votes) as v:

    votes = ct.Counter()
    reader = csv.reader(v)
    next(reader)
    for line in reader:
        candidate = line[-1]
        votes[candidate] += 1
        vote_total += 1

# Print Election Results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_total}")
print("----------------------------")

# Perform and print vote percentage calculations
for candidate in votes:
    percent_total = votes[candidate]/vote_total
    percentage = "{:.3%}".format(percent_total)
    print(f"{candidate}. {percentage} ({votes[candidate]}")

# Print Winner
print("----------------------------")    
print(f"Winner: {votes.most_common(1)[0][0]}" )

print("----------------------------")

# Write to text file
file = open('Analysis/election_results.txt', "w")
file.write("Election Results\n")
file.write("----------------------------\n")
file.write("Total Votes: " + str(vote_total) + "\n")
file.write("----------------------------\n")

for candidate in votes:
    percent_total = votes[candidate]/vote_total
    percentage = "{:.3%}".format(percent_total)
    file.write(candidate + ": " + str(percentage) + "("  + str(votes[candidate]) + ")\n")

file.write("-----------------------------\n")
file.write(f"Winner: {votes.most_common(1)[0][0]}\n")
file.write("-----------------------------\n")
file.close()



