class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                result = True
                 
            seen.add(nums[i])


        return result