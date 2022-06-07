def canSum2_rec(targetsum, value_pool):
    if targetsum==0:
        return True
    elif targetsum<0:
        return False
    for v in value_pool:
        remainder=targetsum-v
        if canSum2_rec(remainder, value_pool) ==True:
            return True
    return False

def canSum_dyn(targetsum, value_pool, cache=dict()):
    if targetsum in cache.keys():
        return cache[targetsum]
    elif targetsum==0:
        return True
    elif targetsum<0:
        return False
    for v in value_pool:
        remainder=targetsum-v    
        if canSum_dyn(remainder, value_pool, cache) ==True:
            cache[targetsum]=True
            return True

    cache[targetsum]=True
    return False



if __name__=="__main__":
    #print(canSum(7,[2,3]))
    #print(canSum2_rec(3000,[7,14]))
    print(canSum_dyn(3000,[7,14]))

 