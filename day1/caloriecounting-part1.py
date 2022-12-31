fhand = open('input.txt')

currentcalorie = 0
caloriesums = []
for line in fhand:
    if line != '\n': # calorie count of a food
        currentcalorie = currentcalorie + int(line)
    elif line == '\n': # reached the end of an elf's list
        caloriesums.append(currentcalorie)
        currentcalorie = 0

print(max(caloriesums)) # answer
