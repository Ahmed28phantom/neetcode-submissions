class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        L = 0
        R = len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] < target:
                L += 1
            elif numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] == target:
                result = [L+1,R+1]
                break
        return result