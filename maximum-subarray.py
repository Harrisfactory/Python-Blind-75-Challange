class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #running sum of numbers
        cur_sum = 0
        
        max_sum = nums[0]
        #add each number to sum and compare this sum to the maximum sum and zero
        for i in range(len(nums)):
            
            cur_sum += nums[i]
            
            if(cur_sum > max_sum):
                max_sum = cur_sum
            if(cur_sum < 0):
                cur_sum = 0
        
        return max_sum