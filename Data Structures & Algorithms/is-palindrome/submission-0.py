class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = False
        s = s.lower()
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char
        inv_s = new_s[::-1]
        if new_s == inv_s:
            output = True
        return output