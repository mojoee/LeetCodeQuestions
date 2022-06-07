def canConstruct(target, wordbank, hashmap=dict()):
    if target=="":
        return True


    
    for word in wordbank:
        if target.startswith(word):
            newword="".join(target.rsplit(word))
            if canConstruct(newword,wordbank, hashmap)==True:
                hashmap[target]=True
                return True
               
    hashmap[target]=False
    return False


if __name__=="__main__":
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeeee"]))

