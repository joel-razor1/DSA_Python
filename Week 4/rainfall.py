#Programming Assignment q1

def rainaverage(a):
    city=[]
    annual_rain=[]
    check_duplicate=[]
    trial={}
    count=0
    avg=0
    suma=0
    rain_dictionary={}
    
    for m in range(0,len(a)):
        city.append(a[m][0])
        annual_rain.append(a[m][1])

    print(city)
    print(annual_rain)
    
    for same_city in range(0,len(city)):
        count=0
        suma=0
        avg=0
        flag=0
        suma=annual_rain[same_city]
        print(suma)
        check_duplicate.append(city[same_city])

        for repeat_2 in check_duplicate:
            if city[same_city]==repeat_2:
                count=count+1
                trial[city[same_city]]=count
            for we_got_you in trial.values():
                if we_got_you==1:
                    flag==1
        
#Something is wrong here.
        for same_city_again in range(same_city+1,len(city)):
            if city[same_city]==city[same_city_again]:
                suma=suma+annual_rain[same_city_again]
                rain_dictionary[city[same_city]]=suma
            elif count==1:    #here we included the player who played only once (because it was not included in the if condition)
                rain_dictionary[city[same_city]]=suma
            
                    
    print(trial)
    print(rain_dictionary)    



rainaverage([("city1",2),("city1",3),("city2",3),("city1",1),("city3",8)])
