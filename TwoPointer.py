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


print(merge([1,2,4,0,0,0],3,[2,5,6],3))