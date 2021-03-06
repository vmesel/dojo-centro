def jokenpo(play1, play2):
    if play1 == play2:
        return 'draw'

    plays = ['scissor'
            , 'paper'
            , 'rock'
            , 'lizard'
            , 'spock'   ]

    index_1 = plays.index(play1)

    if plays[(index_1 + 1) % 5] == play2 or \
       plays[(index_1 + 3) % 5] == play2:
        return 'play1'

    return 'play2'