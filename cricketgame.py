import random


def game():
    player1_score=0
    while True:
        run=random.randint(0,6)
        if(run ==0):
            print("out")
            print(player1_score)
            break
        else:
            player1_score += run
    return player1_score
virat=game()

def game2():
    player2_score=0
    while True:
        run2=random.randint(0,6)
        if(run2==0):
            print("out")
            print(player2_score) 
            break
        else:
            player2_score += run2
    return player2_score
rohit=game2()

if(virat > rohit):
    print("virat win")
else:
    print("rohit win")    




