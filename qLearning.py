

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
    #Initalize the states q(s,a) with small random numbers
    returnSum = 0.0

    for episodeNum in range(numEpisodes):
        # Initalize states and G
        G = 0
        s=blackjack.init()

            
        while s!=-1: #-1 is terminal
            ## Use a uniform random distribution for e greedy selection
            check = numpy.random.uniform(0, 1)
           
            if check < epsilon:
                # Our action is less than epsilon we explore
                # Rand int returns a number between 0, 1
                a=random.randint(0,1)

            else:
                a=scipy.argmax(Q[s, :]) 

            # Take action a, and observe reward G and state sp
            G, sp = blackjack.sample(s,a)

            Q[s,a] = Q[s,a] + ( alpha * ( G + ( gamma*max(Q[sp, : ]) ) - Q[s,a] ) )     
            s = sp

            returnSum = returnSum + G

        if (episodeNum % 10000 == 0 and episodeNum > 0):
            print("Episode: ", episodeNum, "Average Return: ", returnSum/episodeNum)

    print("Final Average Return: ", returnSum/numEpisodes)
    blackjack.printPolicy( policy = lambda x: scipy.argmax(Q[x, :]) );
    return None

bjqLearning()


