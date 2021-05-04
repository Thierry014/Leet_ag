def best(l1):
    profit = 0

    for i in range(1,len(l1)):
        # [7,6,1,2,3,4,5]
        if l1[i] > l1[i-1]:
            profit += l1[i]-l1[i-1]
        
    return profit

print(best([7,1,5,3,6,4]))
print(best([1,2,3,4,5]))