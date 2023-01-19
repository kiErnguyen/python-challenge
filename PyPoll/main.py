# University of California Irvine School of Continuing Education
# Data Analytics & Visualization Boot Camp Module 3 Challenge
# Erik Arbelo-Nguyễn

# Importing necessary module(s).
import csv

# Defining .csv file.
path = '/home/kiernguyen/Desktop/python-challenge/PyPoll/Resources/election_data.csv'
file = open(path)
reader = csv.reader(file)

# Creating a list of lists from the .csv file.
header = next(reader)

data = []
for row in reader:
    Ballot_ID = int(row[0])
    County = (row[1])
    Candidate = (row[2])
    data.append([Ballot_ID, County, Candidate])

# Creating variables for the following loop.
Charles = 0
Diana = 0
Raymon = 0

# Loop using if and elif statements to count votes for each candidate.
for row in data:
    if row[2] == 'Charles Casper Stockham':
        Charles += 1
    elif row[2] == 'Diana DeGette':
        Diana += 1
    elif row[2] == 'Raymon Anthony Doane':
        Raymon += 1

# Calculating the percentage of votes per candidate.
total_votes = Charles + Diana + Raymon

Charles_percent = round(Charles / total_votes * 100, 3)
Diana_percent = round(Diana / total_votes * 100, 3)
Raymon_percent = round(Raymon / total_votes * 100, 3)

# Leveraging a dictionary to find the winner.
candidate_votes = {'Charles Casper Stockham': Charles, 'Diane DeGette': Diana, 'Raymon Anthony Doane': Raymon}
winner = max(candidate_votes, key=candidate_votes.get)

# Print functions outlining the results.
print('Election Results')
print('----------')
print('Total Votes: ' + str(total_votes))
print('----------')
print('Charles Casper Stockham: ' + str(Charles_percent) + '% (' + str(Charles) + ')')
print('Diana DeGette: ' + str(Diana_percent) + '% (' + str(Diana) + ')')
print('Raymon Anthony Doane: ' + str(Raymon_percent) + '% (' + str(Raymon) + ')')
print('----------')
print('Winner: ' + winner)

# Writing the results to a .txt file.
analysis = '/home/kiernguyen/Desktop/python-challenge/PyPoll/analysis/analysis.txt'

with open(analysis, 'w') as file:
    file.write('Election Results')
    file.write('----------')
    file.write('Total Votes: ' + str(total_votes))
    file.write('----------')
    file.write('Charles Casper Stockham: ' + str(Charles_percent) + '% (' + str(Charles) + ')')
    file.write('Diana DeGette: ' + str(Diana_percent) + '% (' + str(Diana) + ')')
    file.write('Raymon Anthony Doane: ' + str(Raymon_percent) + '% (' + str(Raymon) + ')')
    file.write('----------')
    file.write('Winner: ' + winner)



# ễ