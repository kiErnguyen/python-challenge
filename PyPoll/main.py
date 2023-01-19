# University of California Irvine School of Continuing Education
# Data Analytics & Visualization Boot Camp Module 3 Challenge
# Erik Arbelo-Nguyễn

# Importing necessary module(s).
import csv

path = '/home/kiernguyen/Desktop/python-challenge/PyPoll/Resources/election_data.csv'
file = open(path)
reader = csv.reader(file)

header = next(reader)

Charles = 0
Diana = 0
Raymon = 0

data = []
for row in reader:
    Ballot_ID = int(row[0])
    County = (row[1])
    Candidate = (row[2])
    data.append([Ballot_ID, County, Candidate])

for row in data:
    if row[2] == 'Charles Casper Stockham':
        Charles += 1
    elif row[2] == 'Diana DeGette':
        Diana += 1
    elif row[2] == 'Raymon Anthony Doane':
        Raymon += 1

total_votes = Charles + Diana + Raymon

Charles_percent = round(Charles / total_votes * 100, 3)
Diana_percent = round(Diana / total_votes * 100, 3)
Raymon_percent = round(Raymon / total_votes * 100, 3)

candidate_votes = {'Charles Casper Stockham': Charles, 'Diane DeGette': Diana, 'Raymon Anthony Doane': Raymon}
winner = max(candidate_votes, key=candidate_votes.get)

print('Election Results')
print('----------')
print('Total Votes: ' + str(total_votes))
print('----------')
print('Charles Casper Stockham: ' + str(Charles_percent) + '% (' + str(Charles) + ')')