class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        cd = 0
        for i in s:
            if i == "(":
                cd += 1
            elif i == ")":
                depth = max(depth, cd)
                cd -= 1
            else:
                continue
        
        return depth