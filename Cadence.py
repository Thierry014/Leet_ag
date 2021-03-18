def maxSubArray(nums) -> int:
    sums, sum_max  = 0, float('-inf')

    for num in nums:
        sums += num

        if sums > sum_max:
                sum_max = sums
            
        if sums < 0:
                sums = 0 
    
    return sum_max



def maxTwice(nums):
    sums = max_sum = nums[0]

    for i in range(1,len(nums)):
        sums = max(nums[i], nums[i]+sums)
        max_sum = max(max_sum,sums)


    return max_sum



nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(nums))

print(maxTwice(nums))

# cadence 算法 
# sums 到目前节点的和  /  到目前节点的和的最大值
# 再和最大值比较 替换
