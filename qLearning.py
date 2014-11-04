

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

def bjqLearning(Q = numpy.random.rand(182,2)*0.00001, alpha=0.008, gamma = 1, numEpisodes=10000000, epsilon=0):




