class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            w_len = len(word)
            encoded_str += str(w_len) + "#" + str(word)
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            decoded_str.append(word)
            i = j+1+length
        return decoded_str