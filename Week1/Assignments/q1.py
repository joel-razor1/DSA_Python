def f(x):
    d=0
    while x >= 1:
        (x,d) = (x/4,d+1)
    return(d)

c=f(255)
print(c)