filePath = "02/input.txt"
maxColors = {"red": 12, "green": 13, "blue": 14}

def check(set):
    for w in set.split(","):
        count, color = w.strip().split(" ")
        count = int(count)
        if count > maxColors[color]:
            return False
    return True


sum = 0
with open(filePath, "r") as file:
    for line in file:
        line = line.strip()
        game, x = line.split(':')
        gameNo = int(game[5:])
        sets = x.split(";")
        possible = all(check(set) for set in sets)
        if possible:
            sum += gameNo
print(sum)
