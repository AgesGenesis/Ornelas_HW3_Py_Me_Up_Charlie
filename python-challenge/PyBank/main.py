import os
import csv
import numpy as np

csvPath = os.path.join("Resources", "budget_data.csv")
numberOfMonths = 0
total = 0
averageChange = []
greatestIncreaseMonth = ""
greatestIncreaseNumber = 0
greatestDecreaseMonth = ""
greatestDecreaseNumber = 0

with open(csvPath, newline='') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")
    csvHeader = next(csvReader) 
    
    for row in csvReader:
        numberOfMonths = numberOfMonths + 1
        averageChange.append(float(row[1]))
        total = total + float(row[1])
        if float(row[1]) > greatestIncreaseNumber:
            greatestIncreaseMonth = row[0]
            greatestIncreaseNumber = float(row[1])
        elif float(row[1]) < greatestDecreaseNumber:
            greatestDecreaseMonth = row[0]
            greatestDecreaseNumber = float(row[1])
        else:
            continue

#calculating avg from list
averageChange = np.mean(averageChange)

#formating as flaot with 2 decimal places
total = "{:.2f}".format(total)
averageChange = "{:.2f}".format(averageChange) 
greatestIncreaseNumber = "{:.2f}".format(greatestIncreaseNumber)
greatestDecreaseNumber = "{:.2f}".format(greatestDecreaseNumber)

#subtracting one month because the last blank row is being counted
numberOfMonths = numberOfMonths - 1


#printing analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: %s" %(str(numberOfMonths)))
print("Total: $%s" %(str(total)))
print("Average Change: $%s" %(str(averageChange)))
print("Greatest Increase in profits: %s ($%s)" %(str(greatestIncreaseMonth), 
                                                 str(greatestIncreaseNumber)))
print("Greatest Decrease in profits: %s ($%s)" %(str(greatestDecreaseMonth), 
                                                 str(greatestDecreaseNumber)))