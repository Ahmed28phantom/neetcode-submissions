class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        set_nums = set(nums)
        for num in set_nums:
            if num - 1 not in set_nums:
                length = 1
                while num + length in set_nums:
                    length += 1
                if result <= length:
                    result = length
        return result