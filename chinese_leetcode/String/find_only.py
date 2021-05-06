def find_only(str):
    dic = {}

    for char in str:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 0 
    
    print(dic)

    for k,v in dic.items():
        if v==0:
            return str.find(k)
    
    return -1


print(find_only('loveleetcode'))