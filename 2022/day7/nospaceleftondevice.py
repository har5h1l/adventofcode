import re
terminal = open('input.txt')

directory = None
filesystem = {}
for line in terminal:
    line = line.strip()
    splitline = line.split()
    if line.startswith('$'): #command
        if splitline[1] == 'cd': # change directory
            if splitline[2] != '..':
                directory = splitline[1] + ' ' + splitline[2]
            els
    else: # data
        if directory == 'dir /': # everything in the system
            if splitline[0] == 'dir':
                filesystem[line] = filesystem.get(line, {})
            else:
                filesystem[splitline[1]] = filesystem.get(splitline[1], splitline[0])
        elif directory == 'dir ..':
            ...

# unfinished thing