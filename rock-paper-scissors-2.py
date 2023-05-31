import random
for num in range(3):
    print(random.choice(["rock","paper","scissors"]))
options = ['rock', 'paper', 'scissors']
#            0        1          2
choices = options[:]

lives = [1, 1, 1]

#Play Instructions
print("Let's play Rock, Paper, Scissors!")
print("Rock smashes scissors, scissors cuts paper, paper covers rock.")

#math
def scoring (ply1, ply2):
    result = options.index(ply1) - options.index(ply2)
    result = result % 3
    return result
#0 = tie, #1 = player1 W, #2 = Player1 L

#Which Option Beats Which
def thinker (ply, comp1, comp2):
    plyresult = [0, 0, 0] #measures change
    for ply1 in [ply, comp1, comp2]:
        for ply2 in [comp2, comp1, ply]:
            matchresult = scoring (ply1, ply2)
            if ply1 == ply and matchresult == 2:
                plyresult [0] = -1
            if ply1 == comp2 and matchresult == 2:
                plyresult [2] = -1
            if ply1 == comp1 and matchresult == 2:
                plyresult [1] = -1
    lives = [lives[x] + plyresult[x] for x in range(3)]

while True:
    #Randomly Choose One
    comp1choice = random.choice(choices)
    comp2choice = random.choice(choices)

    #Get Input
    plychoice = ""
    while plychoice not in options:
        plychoice = input("Pick one ('rock', 'paper', or 'scissors'): ")
        plychoice = plychoice.lower()

    print("Computer 1", comp1choice, "Computer 2", comp2choice, "Player", plychoice)
    print(thinker(plychoice, comp1choice, comp2choice))
