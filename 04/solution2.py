import re
filePath = "04/input.txt"
regex = r"\d{1,}"
cards = 201 * [1]
with open(filePath, "r") as file:

    for i,line in enumerate(file):
        values = line.strip().split("|")
        winningNumbers = set(re.findall(regex,values[0])[1:])
        myNumbers = set(re.findall(regex,values[1]))
        wins = len(winningNumbers & myNumbers)
        for j in range(wins):
            cards[i+1+j] += cards[i]

print(sum(cards))
