def howSum_rec(targetsum, value_pool):
    if targetsum==0:
        return []
    if targetsum<0:
        return None
    for v in value_pool:
        remainder=targetsum-v
        remainder_result = howSum_rec(remainder,value_pool)
        if remainder_result!=None:
            return remainder_result.append(v)
    return None

def subsetsum(array, num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array,(num - array[0])) 
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)



def howSum_dyn(array, num, cache=dict()):
    if num in cache.keys():
        return cache[num]
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = howSum_dyn(array,(num - array[0])) 
            if with_v:
                cache[num]=[array[0]] + with_v
                return [array[0]] + with_v
            else:
                return howSum_dyn(array[1:],num)


if __name__=="__main__":
    print(subsetsum([2,3], 7))
    print(howSum_dyn([2,3], 7))
    print(subsetsum([5,3,4,7], 7))
    print(howSum_dyn([5,3,4,7], 7))
    print(subsetsum([2,4], 7))
    print(howSum_dyn([2,4], 7))
    #print(subsetsum([3,5,2], 100000))
    print(howSum_dyn([7,14], 300))

