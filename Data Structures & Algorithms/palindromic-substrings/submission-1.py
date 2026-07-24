class Solution:
    def countSubstrings(self, s: str) -> int:
        #at letter i, at +1 and check if palindrome
        #if no continue
        #if yes +1 to prev

        dp =[0] * len(s) #num of palindromes in string s[:i]


        for i in range(len(s)):
            #odd
            l, r = i, i
            dp[i] = dp[i] + dp[i-1]

            while l >= 0 and r < len(s) and s[l] == s[r]:
                dp[i] += 1
                l -= 1
                r += 1
            
            #even
            l, r = i-1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                dp[i] += 1
                l -= 1
                r += 1

        return dp[-1]
