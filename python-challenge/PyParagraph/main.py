import os
import re

checkingFiles = "Y"

while checkingFiles == "Y":
    fileName = input("Exact name of doc you would like to analyze wihtout the extenstion (.txt files in Docs directory only): ")
    try:
        filePath = os.path.join("Docs", fileName + ".txt")
        numberOfSentences = 0
        numberOfWords = 0
        letterCount = 0

        with open(filePath, "r") as file:
            fileLines = file.readline()
            splitLines = re.split("(?<=[.!?]) +", fileLines)
            numberOfSentences = len(splitLines)
            splitWords = re.split(" ", fileLines)
            numberOfWords = len(splitWords)
            for item in splitWords:
                letterCount = letterCount + len(item)


        avgSentenceLength = numberOfWords / numberOfSentences
        avgLettersPerWord = letterCount / numberOfWords


        avgSentenceLength = "{:.1f}".format(avgSentenceLength)
        avgLettersPerWord = "{:.1f}".format(avgLettersPerWord)
        
        print()
        print("Paragraph Analysis")
        print("------------------------")
        print("Approximate Word Count: %s" %(str(numberOfWords)))
        print("Approximate Sentence Count: %s" %(str(numberOfSentences)))
        print("Average Letter Count: %s" %(str(avgLettersPerWord)))
        print("Average Sentence Length: %s" %(str(avgSentenceLength)))

        checkingFiles = input("Would you like to check another file? (Y)es/(N)o: ")
        if checkingFiles != "Y" and checkingFiles != "N":
            while checkingFiles != "Y" and checkingFiles != "N":
                checkingFiles = input("Please type only Y or N to continue or cancel. ")
        elif checkingFiles == "N":
            print("Closing")
    
    except FileNotFoundError:
        checkingFiles = input("The file you entered does not exist would you like to try again? (Y)es/(N)o: ")
        if checkingFiles != "Y" and checkingFiles != "N":
            while checkingFiles != "Y" and checkingFiles != "N":
                checkingFiles = input("Please type only Y or N to continue or cancel. ")
        elif checkingFiles == "N":
            print("Closing")
