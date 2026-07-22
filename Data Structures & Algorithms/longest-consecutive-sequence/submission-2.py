class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        s = sorted(nums)
        longest = 1
        curr = 1

        for i in range(len(s) - 1):
            if s[i + 1] == s[i]:
                continue
            if s[i + 1] == s[i] + 1:
                curr += 1
                if curr > longest:
                    longest = curr
            else:
                curr = 1

        return longest