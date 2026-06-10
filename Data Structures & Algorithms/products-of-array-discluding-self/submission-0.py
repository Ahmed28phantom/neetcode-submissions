class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        for i in range(len(nums)):
            for x in nums[:i]:
                output[i] *= x
            for x in nums[i+1:]:
                output[i] *= x
        return output
