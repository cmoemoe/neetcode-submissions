class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        curr = ""
        longest = ""
        for i in range(len(s)):
            if s[i] in curr:
                if len(curr) > len(longest):
                    longest = curr
                #find index of repeated letter
                curr = curr[curr.find(s[i]) + 1:]
            curr += s[i]
        
        return max(len(curr), len(longest))
