strategyguide = open('input.txt')

# rock(a) = 1
# paper(b) = 2
# scissors(c) = 3
# loss(x) = 0
# tie(y) = 3
# win(z) = 6
totalscore = 0
for game in strategyguide:
    points = 0
    game = game.split()
    if game[0] == 'A': # rock
        if game[1] =='X': # to lose we play scissors
            points = 3
        elif game[1] == 'Y': # to tie we play rock
            points = 4
        elif game[1] == 'Z': # to win we play paper
            points = 8
    elif game[0] == 'B': # paper
        if game[1] == 'X': # to lose we play rock
            points = 1
        elif game[1] == 'Y': # to tie we play paper
            points = 5
        elif game[1] == 'Z': # to win we play scissors
            points = 9
    elif game[0] == 'C': # scissors
        if game[1] == 'X': # to lose we play paper
            points = 2
        elif game[1] == 'Y': # to tie we play scissors
            points = 6
        elif game[1] == 'Z': # to win we play rock
            points = 7
    totalscore = totalscore + points

print(totalscore)