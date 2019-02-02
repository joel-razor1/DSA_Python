def gcd(m,n):
    if (m>n):
        (m,n)=(n,m)

    if (m%n==0):
        return(n)

    else:
        r=m%n
        return(gcd(n,r)) 


a=input()
b=input()
c=gcd(int(a),int(b))
print(c)recursion