idnums = open('input.txt')

containcount = 0
for pair in idnums:
    pair = pair.strip().split(',')
    id1start = int(pair[0].split('-')[0])
    id1end = int(pair[0].split('-')[1])
    id2start = int(pair[1].split('-')[0])
    id2end = int(pair[1].split('-')[1])

    if (id2start <= id1start and id2end >= id1end) or (id1start <= id2start and id1end >= id2end):
            containcount = containcount + 1

print(containcount)