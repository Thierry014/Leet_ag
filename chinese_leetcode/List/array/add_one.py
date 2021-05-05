def addone(l1):
    # [1,2,3,4] => [1,2,3,5]

    res = 0
    l1 = l1[::-1] 
    # [4,3,2,1]

    for i,num in enumerate(l1):
        res += num*pow(10,i)
    
    res += 1
    res_list = []
    print(res)
    while res>0:
        res_list.append(res%10)
        res //= 10
    return res_list[::-1]

print(addone([0]))
