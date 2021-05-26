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






