def rotate(l1,k):
    # a+b
    head = l1[k*-1:]
    l1 = head+l1[:k*-1]
    return l1


print(rotate([1,2,3,4,5,6,7],3))
print(rotate([-1,-100,3,99],2))


def rotate2(l1,k):
    # 3 times rotate
    l1 = l1[::-1]
    l1[:k] = l1[:k][::-1]
    l1[k:] = l1[k:][::-1]

    return l1

print(rotate2([1,2,3,4,5,6,7],3))
print(rotate2([-1,-100,3,99],2))

