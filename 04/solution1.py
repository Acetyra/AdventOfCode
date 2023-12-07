import re

filePath = "04/input.txt"
regex = r"\d{1,}"
sum = 0
with open(filePath, "r") as file:
    for line in file:
        values = line.strip().split("|")
        winningNumbers = set(re.findall(regex,values[0])[1:])
        myNumbers = set(re.findall(regex,values[1]))
        wins = len(winningNumbers & myNumbers)
        if wins > 0:
            sum += 2**(wins-1)

print(sum)
