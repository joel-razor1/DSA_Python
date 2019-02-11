def h(n):
    s = 0
    for i in range(1,n):
        if n%i == 0:
           s = s+i
    return(s)


c=h(28)-h(27)
print(c)