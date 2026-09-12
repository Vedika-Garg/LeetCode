class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = 0

        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if j == i:
                    continue

                for k in range(len(digits)):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 == 0:
                        ans += 1

        # Remove duplicate numbers caused by duplicate digits
        nums = set()

        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if len({i, j, k}) < 3:
                        continue
                    if digits[k] % 2 == 0:
                        nums.add(digits[i] * 100 + digits[j] * 10 + digits[k])

        return len(nums)
        # e = 0
        # o = 0
        # for i in digits:
        #     if i % 2 == 0:
        #         e += 1
        #     else:
        #         o += 1
        
        # if e == 0:
        #     return 0

        # func = {}
        # for i in digits:
        #     if i not in func:
        #         func[i] = 1
        #     func[i] += 1
        
        # n = len(func)
        # if n == 1:
        #     return 1
            
        # if 0 in func:
        #     z = func[0]
        #     ans = z * (n - z) * (n - 2) + (e - z) * (n - z - 1) * (n - 2)
        # else:
        #     ans = e * (n - 1) * (n - 2)
        
        # return ans