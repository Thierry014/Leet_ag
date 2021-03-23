def merge(nums1, m, nums2, n):
    last = m+n-1
    m = m-1
    n = n-1 
        # print(m,n)

    while m>=0 and n>=0:

        if nums1[m]>nums2[n]:
            nums1[last] = nums1[m]
            m -=1
        else:
            nums1[last] = nums2[n]
            n -=1
        last -=1
        
    if n>=0:
            nums1[:last+1] = nums2[:n+1]

    return nums1


# print(merge([1,2,4,0,0,0],3,[2,5,6],3))



def mergeNew(n1, m, n2, n):
    res = [i for i in range(m+n)]
    last = m+n-1

    m = m-1
    n = n-1

    while n>=0 and m>=0:
        if n1[m] > n2[n]:
            res[last] = n1[m]
            m -= 1
        else:
            res[last] = n2[n]
            n -=1
        last -=1
    if m>=0:
        res[:last+1] = n1[:m+1]
    else:
        res[:last+1] = n2[:n+1]
    
    return res

print(mergeNew([1,2,4,0,0,0],3,[2,5,6],3))
