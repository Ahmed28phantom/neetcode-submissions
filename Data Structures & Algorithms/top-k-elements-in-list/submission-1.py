from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = Counter(nums)
        for element, count in counts.most_common(k):
            result.append(element)
        return result