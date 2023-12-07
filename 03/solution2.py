filePath = "03/input.txt"

grid = []
with open(filePath, "r") as file:
    for line in file:
        grid.append(list(line.strip()))
def findNumber(matrix,row, col):
    num = matrix[row][col]

    if (col < len(matrix[0]) - 1 and matrix[row][col + 1].isdigit()):
        num += matrix[row][col + 1]
        if (col < len(matrix[0]) - 2 and matrix[row][col + 2].isdigit()):
            num += matrix[row][col + 2]

    if (col > 0 and matrix[row][col - 1].isdigit()):
        num = matrix[row][col - 1] + num
        if (col > 1 and matrix[row][col - 2].isdigit()):
            num = matrix[row][col - 2] + num


    return num


def isAdjacent(matrix, target_char, row, col):
    nums = []
    # Check left
    if col > 0 and matrix[row][col - 1] in target_char:
        nums.append(int(findNumber(matrix, row, col-1)))
    # Check right
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] in target_char:
        nums.append(int(findNumber(matrix, row, col+1)))
    # Check up
    if row > 0 and matrix[row - 1][col] in target_char:
        nums.append(int(findNumber(matrix, row-1, col)))
    # Check down
    if row < len(matrix) - 1 and matrix[row + 1][col] in target_char:
        nums.append(int(findNumber(matrix, row+1, col)))
    # Diagonal up-left
    if row > 0 and col > 0 and matrix[row - 1][col - 1] in target_char:
        nums.append(int(findNumber(matrix, row-1, col-1)))
    # Diagonal up-right
    if row > 0 and col < len(matrix[0]) - 1 and matrix[row - 1][col + 1] in target_char:
        nums.append(int(findNumber(matrix, row-1, col+1)))
    # Diagonal down-left
    if row < len(matrix) - 1 and col > 0 and matrix[row + 1][col - 1] in target_char:
        nums.append(int(findNumber(matrix, row+1, col-1)))
    # Diagonal down-right
    if row < len(matrix) - 1 and col < len(matrix[0]) - 1 and matrix[row + 1][col + 1] in target_char:
        nums.append(int(findNumber(matrix, row+1, col+1)))
    return nums       

number = ""
sum = 0
isPart = False
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == "*":
            res = list(set(isAdjacent(grid, "1234567890", y,x)))
            if len(res) == 2:
                sum += res[0] * res[1]

print(sum)
            