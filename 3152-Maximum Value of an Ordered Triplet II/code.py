class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        #O(N^2)
        # left=nums[0]
        # res=0

        # for j in range(1,len(nums)):
        #     if nums[j]>left:
        #         left=nums[j]
        #     for i in range(j+1,len(nums)):
        #         res=max(res,(left-nums[j])*nums[i])
        # return res


        #O(N)

        # first we get the prefix sum and do a max_diff and then we will get the result 
        prefix_max=nums[0]
        res=0
        max_diff=0
        for k in range(1,len(nums)):
            prefix_max=max(prefix_max,nums[k])
            res=max(res,max_diff * nums[k])
            max_diff=max(max_diff,prefix_max-nums[k])
        return res
