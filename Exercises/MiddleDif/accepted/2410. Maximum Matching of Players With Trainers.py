def matchPlayersAndTrainers(players,trainers):
    counter = 0
    players.sort()
    trainers.sort()
    gc = 0
    sc = 0

    while gc< len(players) and sc < len(trainers):
        if players[gc] <= trainers[sc]:
            counter+=1
            gc+=1
        sc+=1

    return counter

print(matchPlayersAndTrainers([1,2,1,1,1,1,4],[1,2,3,7,8]))

