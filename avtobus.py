tc = int(input())

while tc >0:
    possible=False
    n=int(input())
    #n=4*x+6*y
    maximum=n//4
    minimum=n//6
    for i in range(minimum, maximum):
        n%
        if 4*minimum==n:
            possible=True
            break
    if possible:
        print(n/4, n/6)
    else:
        print(-1)
    tc-=1
