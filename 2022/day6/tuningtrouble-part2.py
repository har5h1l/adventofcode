buffer = open('input.txt').read().strip()

characters = ['']
for char in buffer:
    characters.append(char)
characters = tuple(characters)

n = 0
for char in characters:
    charfourteen = set(characters[n:n+14])
    if len(charfourteen) == 14:
        markerpos = n + 13
        break
    n = n + 1

print(markerpos)