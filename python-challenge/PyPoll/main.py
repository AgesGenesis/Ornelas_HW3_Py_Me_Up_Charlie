import os
import csv
import operator

csvPath = os.path.join("Resources", "election_data.csv")
totalVotes = 0
candidateList = []
votesByCandidate = {}
candidatePercentage = {}


with open(csvPath, newline = "") as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")
    csvHeader = next(csvReader)
    
    for row in csvReader:
        totalVotes = totalVotes + 1
        if row[2] not in candidateList:
            candidateList.append(row[2])
            votesByCandidate[row[2]] = 0
        else:
            votesByCandidate[row[2]] = votesByCandidate[row[2]] + 1


for item in candidateList:
    candidatePercentage[item] = (votesByCandidate[item] / totalVotes) * 100
    candidatePercentage[item] = "{:.3f}".format(candidatePercentage[item])


winner = max(votesByCandidate.items(), key = operator.itemgetter(1))[0]

separator = "--------------------------"
print("Election Results")
print(separator)
print(totalVotes)
print(separator)
for item in candidateList:
    print("%s: %s%% (%s)" %(str(item), 
                            str(candidatePercentage[item]), 
                            str(votesByCandidate[item])))
print(separator)
print("Winner: %s" %(str(winner)))
print(separator)