def rps(p1, p2):
# 1st solution
    if p1 == p2:
        return "Draw!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    else:
        return "Player 2 won!"

# 2nd solution
    # beat = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    # if p1 == p2:
    #     return 'Draw!'
    # elif beat[p1] == p2:
    #     return 'Player 1 won!'
    # else:
    #     return 'Player 2 won!'






print(rps('rock', 'scissors'))   #  "Player 1 won!"
print(rps('scissors', 'rock'))   #  "Player 2 won!"
print(rps('rock', 'rock'))       #  'Draw!'