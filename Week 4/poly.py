#practice assignment question2

def addpoly(p1,p2):
    p1c=[]
    p2c=[]
    p1e=[]
    p2e=[]
    result=[]
    for ic in p1:
        p1c.append(ic[0])
    for ie in p1:
        p1e.append(ie[1])
    for jc in p2:
        p2c.append(jc[0])
    for je in p2:
        p2e.append(je[1])
    print(p1c)
    print(p1e)
    print(p2c)
    print(p2e)      
    for i in range(0,len(p1e)):
        for j in range(0,len(p2e)):
            if p1e[i]==p2e[j]:
                result.append((p1c[i]+p2c[j],p1e[i]))
            elif 

    return result    



a=addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
print(a)
