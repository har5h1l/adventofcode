buffer = open('input.txt').read().strip()

characters = ['']
for char in buffer:
    characters.append(char)

n = 0
for char in characters:
    charfour = {char, characters[n + 1], characters[n + 2], characters[n + 3]}
    if len(charfour) == 4:
        markerpos = n + 3
        break
    n = n + 1

print(markerpos)