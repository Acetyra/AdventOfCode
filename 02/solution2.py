filePath = "02/input.txt"

def check(set):
    maxValues = {"red":0,"green": 0,"blue": 0}
    for w in set.split(","):
        count, color = w.strip().split(" ")
        count = int(count)
        maxValues[color] = max(maxValues[color], count)
    return maxValues


sum = 0
with open(filePath, "r") as file:
    for line in file:
        line = line.strip()
        game, x = line.split(':')
        gameNo = int(game[5:])
        sets = x.split(";")
        result = [check(set) for set in sets]
        red = green = blue = 0
        for i in result:
            red = max(red, i["red"])  
            green = max(green, i["green"])
            blue = max(blue, i["blue"])
        sum += (red*green*blue)
print(sum)
