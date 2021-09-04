import os,pdb
import csv

polling_csv = os.path.join("Resources/election_data.csv")


file = "election_data.csv"

total_votes = []
candidates = []
average = []
unique_list = []
khan1 = []
correy1 = []
li1 = []
otooley1 = []

with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        
        total_votes.append(row[0])
        candidates.append(row[2])
        
        if row[2] == str("Khan"):
            khan1.append(khan1)

        if row[2] == str("Correy"):
            correy1.append(correy1)

        if row[2] == str("Li"):
            li1.append(li1)

        if row[2] == str("O'Tooley"):
            otooley1.append(otooley1)


text_file = open("Election Results (d-pranjic).txt", "w")

text_file.write(print("Election Results"),
    print("__________________"),
    print("Total Votes:", len(total_votes)),
    print("__________________"),
    print("Khan:","{:.2%}".format((len(khan1)/len(total_votes))), '({})'.format(len(khan1))),
    print("Correy:","{:.2%}".format((len(correy1)/len(total_votes))), '({})'.format(len(correy1))),
    print("Li:","{:.2%}".format((len(li1)/len(total_votes))), '({})'.format(len(li1))),
    print("O'Tooley:","{:.2%}".format((len(otooley1)/len(total_votes))), '({})'.format(len(otooley1))),
    print("__________________"),
    print("Winner: Khan"),
    print("__________________"))

text_file.close()