#Practice Assignment Question 1

def orangecap(a):
    matches=[]
    players=[]
    scores=[]
    check_duplicate=[]
    player_sum={}
    count=0
    suma=0
    for m in a:
        matches.append(m)
        for p in a[m]:
            players.append(p)
            scores.append(a[m][p])


    for same in range(0,len(players)):
        suma=0
        suma=scores[same]
        for yessame in range(same+1,len(players)):
            if players[same]==players[yessame]:
                suma=suma+scores[yessame]
                print(suma)
                player_sum[players[same]]=suma
    return player_sum
"""
        suma=0
        suma=scores[same]
        check_duplicate.append(players[same])
        
            
        for yessame in range (same+1,len(players)):
            suma=suma+scores[yessame]
            player_sum[players[same]]=suma
        #count=0
    
            print(suma)
    #return player_sum
"""

player=orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
print(player)
