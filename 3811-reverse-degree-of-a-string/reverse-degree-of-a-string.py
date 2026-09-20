class Solution:
    def reverseDegree(self, s: str) -> int:
        rd = 0
        
        for i in range(len(s)):
            val = 123 - ord(s[i])
            prod = val * (i+1)
            rd += prod
        
        return rd