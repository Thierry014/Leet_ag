def containsNearbyDuplicate(nums, k):
    hashtable = {} 
        # {1:0 2:1 value:index}
        
    for i in range(len(nums)):
        if nums[i] in hashtable and i - hashtable[nums[i]] <= k:
                    return True

            # keep update the index 
        hashtable[nums[i]] = i
            
    return False

#  find duplicate distance
print(containsNearbyDuplicate([1,2,3,1],3))