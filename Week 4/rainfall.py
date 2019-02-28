#Programming Assignment q1

def rainaverage(a):
    city=[]
    annual_rain=[]
    check_duplicate=[]
    trial={}
    count=0
    avg=0
    suma=0
    rain_sum={}
    
    for m in range(0,len(a)):
        city.append(a[m][0])
        annual_rain.append(a[m][1])

   

    for same in range(0,len(city)):
        count=0
        suma=0
        flag=0
        suma=annual_rain[same]  
        check_duplicate.append(city[same])

        
        for repeat_2 in check_duplicate:
            
            if city[same]==repeat_2:
                count=count+1                
                trial[city[same]]=count
            for we_got_you_too in trial.values():
                if we_got_you_too==1:
                    flag=1    

        for yessame in range(same+1,len(city)):
            if city[same]==city[yessame]:
                suma=suma+annual_rain[yessame]
                rain_sum[city[same]]=suma
            elif count==1:    
                rain_sum[city[same]]=suma

    v=list(rain_sum.values())    
    k=list(rain_sum.keys())
    c=list(trial.values()) 
    final_list=[]
    final_final_list=[]
    for i in range(0,len(v)):
        final_list.append(float(v[i]/c[i]))
       
    final_final_dict={}
    final_final_dict_sorted={}
    for j in range(0,len(k)):
        final_final_dict[k[j]]=final_list[j]
    for key in sorted(final_final_dict):
        final_final_dict_sorted[key]=final_final_dict[key]

    v2=list(final_final_dict_sorted.values())
    k2=list(final_final_dict_sorted.keys())
    for h in range (0,len(v2)):
        final_final_list.append((k2[h],v2[h]))
    return final_final_list
        

b=rainaverage([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)])
print(b)

#The following test case is not satisfied
#rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])
