#Practice Assignment Question 1

def orangecap(a):
    matches=[]      #a list to keep track of matches
    players=[]      # a list to keep the track of players matching with the same index as of list scores
    scores=[]       # a list to keep the track of scores of each players of same index in list players
    check_duplicate=[] # this list was made to keep track of how many times the player played in the tournament
    player_sum={}   #this dictionary is made to show total score of each players
    trial={}    #this dictionary is made to see the duplicate entries and keep a count on it.
    count=0
    suma=0
    #the following loop segregates the input data in the appropriate lists
    for m in a:
        matches.append(m)
        for p in a[m]:
            players.append(p)
            scores.append(a[m][p])

    #mother loop
    for same in range(0,len(players)):
        count=0
        suma=0
        flag=0
        suma=scores[same]  #first player score is assigned now itself
        check_duplicate.append(players[same]) # appending the name to the duplicate list

        #this loop is made (main purpose) to identfy the player who have played only once(flag process)
        for repeat_2 in check_duplicate:
            
            if players[same]==repeat_2:
                count=count+1                
                trial[players[same]]=count
            for we_got_you_too in trial.values():
                if we_got_you_too==1:
                    flag=1
        #this loop is made to calculate the total scores
        for yessame in range(same+1,len(players)):
            if players[same]==players[yessame]:
                suma=suma+scores[yessame]
                #print(suma)
                player_sum[players[same]]=suma
            elif count==1:    #here we included the player who played only once (because it was not included in the if condition)
                player_sum[players[same]]=suma
    v=list(player_sum.values()) #in this the value of player_sum is converted to list
    k=list(player_sum.keys()) #in this the key of player_sum is converted to list
    i=v.index(max(v))   #max value is found and index is stored
    return (k[i],v[i])  #returned the pair as asked in the question

player=orangecap()
print(player)

#test inputs
#{'match1':{'player1':57, 'player2':138}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}
#{'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91},'test1':{'Ashwin':84, 'Kohli':120}, #'test2':{'ashwin':59, 'Pujara':42}}
