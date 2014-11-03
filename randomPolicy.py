import blackjack

import numpy
import random
import scipy 

def showOneGame():
    s=blackjack.init()
    moves=[0,1,0] 
    turn=0
    while s!=-1: #-1 is terminal
        a=moves[turn]
        r,sp=blackjack.sample(s,a)
        print("turn %d: s %d a %d -> r %d sp %d "%(turn,s,a,r,sp),end="")
        print("\t Player Sum: %d  Dealer Card: %d  Usable Ace: %d"%(blackjack.playerSum,blackjack.dealerCard, blackjack.usableAce))
        s=sp
        turn+=1
    return None

def bjrandomPolicy(numEpisodes=10000):
    # Input: number of Episodes
    # Output: Average Return over number of episodes
    # Policy: Equally Random
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = 0
        # Implement equaly random probability assuming gamma = 1
        s=blackjack.init()
        while s!=-1: #-1 is terminal
            # Rand int returns a number between 0, 1
            a=random.randint(0,1)
            G,sp=blackjack.sample(s,a)
            s=sp
        print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G

    print("Average return: ", returnSum/numEpisodes)
    return None

bjrandomPolicy()

