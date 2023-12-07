filePath = "03/input.txt"

grid = []
with open(filePath, "r") as file:
    for line in file:
        grid.append(list(line.strip()))

def isAdjacent(matrix, target_char, row, col):
    # Check left
    if col > 0 and matrix[row][col - 1] in target_char:
        return True
    # Check right
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] in target_char:
        return True
    # Check up
    if row > 0 and matrix[row - 1][col] in target_char:
        return True
    # Check down
    if row < len(matrix) - 1 and matrix[row + 1][col] in target_char:
        return True
    # Diagonal up-left
    if row > 0 and col > 0 and matrix[row - 1][col - 1] in target_char:
        return True
    # Diagonal up-right
    if row > 0 and col < len(matrix[0]) - 1 and matrix[row - 1][col + 1] in target_char:
        return True
    # Diagonal down-left
    if row < len(matrix) - 1 and col > 0 and matrix[row + 1][col - 1] in target_char:
        return True
    # Diagonal down-right
    if row < len(matrix) - 1 and col < len(matrix[0]) - 1 and matrix[row + 1][col + 1] in target_char:
        return True
    return False       

number = ""
sum = 0
isPart = False
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == ".":

            pass
        if char.isdigit():
            number += char
            # check if part
            if isAdjacent(grid, "*#$&=+-%@/", y,x):
                isPart = True
            # end of number check
            if ((x < len(grid[y]) - 1 and not grid[y][x + 1].isdigit()) 
                # check if number is last digit in row
                or x == len(grid[y]) - 1): 
                if isPart == True:
                    sum += int(number)
                isPart = False
                number = ""
                continue
print(sum)
            