import re

filePath = "01/input.txt"
regex = r"\d"
sum = 0
with open(filePath, "r") as file:
    for line in file:
        numbers = re.findall(regex, line)
        number = int(numbers[0] + numbers[-1])
        print(number)
        sum += number
print(sum)