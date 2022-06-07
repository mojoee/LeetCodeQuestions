n,q=[int(x) for x in input().split(" ")]
#a = [int(x) for x in input().split(" ")]
a = list(map(int, input().split(" ")))

while q >0:
    t=input()
    if t[0]=="1":
        _, i, x=t.split(" ")
        i,x =int(i), int(x)        
        a[i-1]=x

    else:
        _, x = t.split(" ")
        a=[int(x)] * len(a)
    print(sum(a))

    q-=1
