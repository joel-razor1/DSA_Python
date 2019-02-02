def imgcd(m,n):
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            mcrf=i

    return mcrf

a=input()
b=input()
c=imgcd(int(a),int(b))
print(c)