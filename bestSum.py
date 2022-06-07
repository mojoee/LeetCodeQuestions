def bestSum(targetsum, numbers):
    if targetsum==0:
        return []
    elif targetsum<0:
        return None
    shortest_combination_len=0
    shortest_combination=[]

    for number in numbers:
        remainder = targetsum-number
        remainderCombination=bestSum(remainder, numbers)
        if remainderCombination!=None:
            remainderCombination.append(number)
            if len(remainderCombination)<len(shortest_combination):
                shortest_combination=remainderCombination

if __name__=="__main__":
    print(bestSum(7,[5,3,4,7]))