def convertToTitle(num):
    last = 0 
    strlist =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        
    res = []
    if num <= 26:
        res = [num]

    while num > 26:
        last = num%26
        num //= 26
        res.insert(0,last)
            
        if last == 0:
                num -=1
            
        if num <= 26:
            res.insert(0,num)

    for i, v in enumerate(res):
            res[i] = strlist[v-1]
        
    return ('').join(res)
            
            
print(convertToTitle(1250))


