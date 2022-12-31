idnums = open('input.txt')

overlap = 0
for pair in idnums:
    pair = pair.strip().split(',')
    id1start = int(pair[0].split('-')[0])
    id1end = int(pair[0].split('-')[1])
    id2start = int(pair[1].split('-')[0])
    id2end = int(pair[1].split('-')[1])

    if (id1start <= id2end and id1start >= id2start) or (id1end <= id2end and id1end >= id2start) or (id2start <= id1end and id2start >= id1start) or (id2end <= id1end and id2end >= id1start):
            overlap = overlap + 1

print(overlap)