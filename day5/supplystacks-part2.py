import re

supplystacks = open('input.txt', 'r') 
yheight = 0
for line in supplystacks: # height calculation
    if line[0] == ' ':
        break
    else:
        yheight = yheight + 1

supplystacks = open('input.txt', 'r') # repopening the file because it doesn't reread lines
i = 1
stacks = dict()
for data in supplystacks:
    for n in range(1, 10): # in each line we go through 1 - 9, grab all the values, and assign it to its corresponding key
        stacks[n] = stacks.get(n, [])
        if data[1 + 4*(n-1)] != ' ': # making sure we don't add a blank value
            stacks[n].append(data[1 + 4*(n-1)])
        n = n + 1
    i = i + 1
    if i > yheight: # break condition
        break

for instruction in supplystacks:
    if instruction.startswith('move') == False:
        continue
    move = int(re.findall('move\s([0-9]*)', instruction.strip())[0]) # move instruction
    fromwhere = int(re.findall('move\s[0-9]*\sfrom\s([0-9]*)', instruction.strip())[0]) # from instruction
    to = int(re.findall('move\s[0-9]*\sfrom\s[0-9]*\sto\s([0-9]*)', instruction.strip())[0]) # to instruction
    for i in range(move):
        stacks[to].insert(0, str(stacks[fromwhere][(move - i - 1)]))
        stacks[fromwhere].pop(move - i - 1)

print(stacks[1][0] + stacks[2][0] + stacks[3][0] + stacks[4][0] + stacks[5][0] + stacks[6][0] + stacks[7][0] + stacks[8][0] + stacks[9][0]) # RGLVRCQSB