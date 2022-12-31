rucksacks = open('input.txt')

commonitems = []
for rucksack in rucksacks:
    length = len(rucksack)
    compartment1 = rucksack[: length//2]
    compartment2 = rucksack[length//2:]
    print(compartment1, compartment2)
    for item in compartment1:
        if item in compartment2:
            commonitems.append(item)
            break

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalpriority = 0
for item in commonitems:
    priority = alphabet.index(item) + 1
    totalpriority = totalpriority + priority
    print(item, priority, totalpriority)

print(totalpriority)
