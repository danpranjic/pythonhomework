# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

# Files to load (Remember to change these)
file = "budget_data.csv"

total = []
date = []
average = []

with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:

        total.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("__________________")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(total))

    for i in range(1,len(total)):
        average.append(total[i] - total[i-1])   
        averageaverage = sum(average)/len(average)

        maximus = max(average)

        minimus = min(average)

        max_date = str(date[average.index(max(average))])
        min_date = str(date[average.index(min(average))])


    print("Avereage Revenue Change: $", round(averageaverage))
    print("Greatest Increase in Revenue:", max_date,"($", maximus,")")
    print("Greatest Decrease in Revenue:", min_date,"($", minimus,")")