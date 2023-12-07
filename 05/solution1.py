filePath = "05/input.txt"

class seed:
    soil : int 
    fertilizer : int
    water : int
    light : int
    temperature : int
    humidity : int
    location : int

sum = 0
with open(filePath, "r") as file:
    a = file.readlines()
    for line in file:
        print("a")