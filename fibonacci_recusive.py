def fibonacci_rec(n, cache=dict()):
    pass

def fibonacci_dyn(n, cache=dict()):
    cache[1]=1
    cache[2]=1
    for i in range(2,n):
        cache[n]=cache[n-1]+cache[n-2]
    return cache[n]    


if __name__=="__main__":
    for i in range(1,50):
        print(f" {i}: {fibonacci_dyn(i)}")