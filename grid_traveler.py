import numpy as np
def gridTraveler_rec(m,n):
    if m==0 or n==0:
        return 0
    elif m==1 and n==1:
        return 1
    else:
        return gridTraveler_rec(m-1,n) +  gridTraveler_rec(m, n-1)

def gridTraveler_dyn(m, n, memo=dict()):
    for key in memo.keys():
        if key==(m,n):
            return memo[m,n]
    if m==0 or n==0:
        return 0
    elif m==1 and n==1:
        return 1

    memo[m,n]=gridTraveler_dyn(m-1,n, memo) +  gridTraveler_dyn(m, n-1, memo)
    return memo[m,n]


if __name__=="__main__":
    #print(gridTraveler_rec(3,3))
    print(gridTraveler_dyn(32,18))
