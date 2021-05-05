def twosum(l1,k):
    # [2,3,7,8,10] => 9 => [0,2]
    dic = {}

    for i, num in enumerate(l1):
        target = k - num

        if target in dic:
            return [dic[target],i]
        else:
            dic[num] = i

print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))
print(twosum([3,3],6))