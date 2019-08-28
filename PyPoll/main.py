import csv
import os

votes = []
# Find the folder path of the executing python script to correctly locate the excel file no matter where it is
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'election_data.csv')) as election_data_file:
    election_data = csv.DictReader(election_data_file)
    # Iterate through each row in excel data one by one and get corresponding vote (selected Candidate by a voter)
    for row in election_data:
        votes.append(row['Candidate'])

result = 'Election Results\n--------------------------------------\n'
# Total number of votes is equal to the length of the votes
result += 'Total Votes: %d\n' % len(votes)
result += '--------------------------------------\n'

# The votes list includes all votes. Turning it into a set (unique elements) gives us the list of candidates.
candidates = set(votes)

# Calculate the number of votes for each candidate, create a tuple (candidate, vote) and add it in election_results
candidate_results = []
for candidate in candidates:
    candidate_results.append((candidate, votes.count(candidate)))

# Sort the election_results list of tuples in descending (reverse=True) order of votes for candidates
candidate_results.sort(key=lambda x: x[1], reverse=True)

for candidate_result in candidate_results:
    # each result is a tuple that has candidate name and vote.
    # result[0] includes candidate name, and result[1] includes the votes of that candidate.
    result += '%s: %.4f%% (%d)\n' % (candidate_result[0], candidate_result[1] / len(votes) * 100, candidate_result[1])

result += '--------------------------------------\n'
# The winner is the candidate of the first element in the election_results list
result += 'Winner: %s\n' % candidate_results[0][0]
result += '--------------------------------------'

# Write results to the terminal
print(result)

# Write results to a text file
with open(os.path.join(__location__, 'result.txt'), 'w') as result_file:
    result_file.write(result)
