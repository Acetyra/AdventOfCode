import re

filePath = "01/input.txt"
regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
wordToDigit= {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
sum = 0
with open(filePath, "r") as file:
    for line in file:
        numbers = re.findall(regex, line.strip())
        number = [wordToDigit[word] if word.isdigit() is False else int(word) for word in numbers]
        num = 10 * number[0] + number[-1]
        sum += num
print(sum)