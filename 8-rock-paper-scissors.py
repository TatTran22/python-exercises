# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock


def game(player1: str, player2: str) -> int:
    list = ['rock', 'scissor', 'paper']
    winCase = [[0, 1], [1, 2], [2, 0]]
    if player1 not in list or player2 not in list:
        return -1
    if player1 == player2:
        return 0

    currentCase = [list.index(player1), list.index(player2)]
    if currentCase in winCase:
        return 1
    else:
        return 2


startNewGame = True
while startNewGame:
    newGame = str(input('Do you want to start new game? (y/n) ')).lower()
    if newGame != 'y':
        break
    player1 = str(input('Player 1 (rock/scissor/paper): ')).lower()
    player2 = str(input('Player 2 (rock/scissor/paper): ')).lower()
    result = game(player1, player2)

    if result == 0:
        print('Draw!')
    elif result == 1 or result == 2:
        print('Player {} won!'.format(result))
    else:
        print('Invalid input!')
