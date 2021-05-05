def move_zero(l1):
    count = 0

    for num in l1:
        if num == 0:
            count +=1
            l1.remove(0)
    

    if count > 0:
        for i in range(count):
            l1.append(0)

    return l1

print(move_zero([0,1,0,3,12]))



