import os
import csv
print(os.getcwd())
csvpath = ".\\PyPoll\\Resources\\election_data.csv"

totalvotes = 0
votepercent = 0
# charlesvotes = 0
# dianavotes = 0
# raymondvotes = 0

candidatelist = []

candidatedict = {}


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)


    for row in csvreader:
        totalvotes += 1 

        candidatename = str(row[2])
           
        if candidatename not in candidatelist:
            candidatelist.append(candidatename)
            candidatedict[candidatename] = 0

    
        candidatedict[candidatename] += 1


output = f"""
Election Results
-------------------------
Total Votes: {totalvotes:,}
-------------------------
"""
winner = ""
winningvotes = 0

for candidatename in candidatelist:
    votes = candidatedict[candidatename]
    if votes > winningvotes:
        winner = candidatename
        winningvotes = votes
    votepercent = votes / totalvotes * 100
    output += f"{candidatename}: {votepercent:,.2f}% ({votes}) \n" 
output += "------------------------- \n"
output += f"Winner: {winner} \n"
output += "-------------------------"

print(output)

with open(".\\PyPoll\\Analysis\\election_analysis.txt", "w") as outputfile:
    outputfile.write(output)