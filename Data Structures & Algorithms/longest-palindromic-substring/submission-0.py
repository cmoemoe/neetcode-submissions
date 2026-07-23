class Solution:
    def longestPalindrome(self, s: str) -> str:
        # def isPalindrome(s):
        #     for i in range(len(s)//2):
        #         if s[i] != s[-1-i]:
        #             return False
        #         return True
        #O(n)
        #have to apply on n^2 substrings so total complexity = O(n^3)

        #can also check if palindrome by looking @ center and seeing if either side is equal
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd len palidromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l-=1
                r+=1

            #even lenth palindromes
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > resLen:
                    res = s[l:r+1]
                    resLen =  r - l + 1
                l-=1
                r+=1

        return res
            
