def only_one(l1):
    dic = {}

    for num in l1:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 0 
    
    return [ k for k, v in dic.items() if v == 0 ]


print(only_one([1,2,1,2,4]))