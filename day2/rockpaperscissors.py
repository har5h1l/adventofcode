strategyguide = open('input.txt')

# rock(a, x) = 1
# paper(b, y) = 2
# scissors(c, z) = 3
# win = 6
# loss = 0
# tie = 3
totalscore = 0
for game in strategyguide:
    points = 0
    game = game.split()
    if game[0] == 'A':
        if game[1] == 'X': # tie
            points = 4
        elif game[1] == 'Y': # win
            points = 8
        elif game[1] == 'Z': # lost
            points = 3
    elif game[0] == 'B':
        if game[1] == 'X': # lost
            points = 1
        elif game[1] == 'Y': # tie
            points = 5
        elif game[1] == 'Z': # win
            points = 9
    elif game[0] == 'C':
        if game[1] == 'X': # win
            points = 7
        elif game[1] == 'Y': # lost
            points = 2
        elif game[1] == 'Z': # tie
            points = 6
    totalscore = totalscore + points

print(totalscore)