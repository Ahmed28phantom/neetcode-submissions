class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}

        for word in strs:
            sort_tuple = tuple(sorted(word))

            if sort_tuple not in group_dict:
                group_dict[sort_tuple] = []

            group_dict[sort_tuple].append(word)
        
        return list(group_dict.values())