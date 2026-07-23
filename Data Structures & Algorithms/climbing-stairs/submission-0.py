class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        
        dp = [0] * (n+1) #distinct ways to reach step i
        #dp[i] = dp[i-1] + dp[i-2] the only way to reach i is from the step before or two steps before
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
