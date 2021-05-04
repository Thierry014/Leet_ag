def find_same(l1,l2):
    if len(l1) > len(l2):
        long = l1
        short = l2
    else:
        long = l2
        short = l1
    
    res = [] 

    for num in short:
        if num in long:
            res.append(num)
            index = long.index(num)
            # long[index] = ''
            long.pop(index)
    return res

print(find_same([1,2,2,1],[2,2]))
print(find_same([4,9,5],[9,4,9,8,4]))
    
