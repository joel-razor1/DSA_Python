#practice assignment question2

def addpoly(p1,p2):
    poly1_coeff=[]
    poly2_coeff=[]
    poly1_exp=[]
    poly2_exp=[]
    add_coeff=[]
    count=0
    flag=[]

    #inserting the coeficients and lists into seperate lists.
    for i in range(0,len(p1)):
        poly1_coeff.append(p1[i][0])
        poly1_exp.append(p1[i][1])
    for j in range(0,len(p2)):
        poly2_coeff.append(p2[j][0])
        poly2_exp.append(p2[j][1])

    #sorting the polynomial in higher order first
    for i in range(0,len(poly1_exp)):
        for j in range(0,len(poly1_exp)):
            if poly1_exp[i]>poly1_exp[j]:
                (poly1_exp[i],poly1_exp[j])=(poly1_exp[j],poly1_exp[i])
                (poly1_coeff[i],poly1_coeff[j])=(poly1_coeff[j],poly1_coeff[i])

    for i in range(0,len(poly2_exp)):
        for j in range(0,len(poly2_exp)):
            if poly2_exp[i]>poly2_exp[j]:
                (poly2_exp[i],poly2_exp[j])=(poly2_exp[j],poly2_exp[i])
                (poly2_coeff[i],poly2_coeff[j])=(poly2_coeff[j],poly2_coeff[i])

    print(poly1_coeff)
    print(poly1_exp)
    print(poly2_coeff)
    print(poly2_exp)
    """            
    for i in range(0,len(poly1_exp)):
        for j in range(0,len(poly2_exp)):
            if poly1_exp[i]==poly2_exp[j]:
                count=count+1
            if count==0:
                flag.append(1)
    print(flag)     
    """
    
    #for pol1e in range(0,len(poly1_exp)):
     #   for pol2e in range(0,len(poly2_exp)):
      #      if poly1_exp[pol1e]==poly2_exp[pol2e]:
       #         add_coeff.append(poly1_coeff[pol1e]+poly2_coeff[pol2e])

    
                





a=addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
print(a)
