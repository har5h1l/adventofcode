rucksacks = open('input.txt')
rucksacks = rucksacks.read().strip().splitlines()

commonitems = []
for i in range(0, len(rucksacks)):
    if 3*i + 1 > len(rucksacks):
        break
    for item in rucksacks[3*i]:
        if item in rucksacks[(3*i + 1)] and item in rucksacks[(3*i + 2)]:
            commonitems.append(item)
            break

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalpriority = 0
for item in commonitems:
    priority = alphabet.index(item) + 1
    totalpriority = totalpriority + priority


print(totalpriority)
