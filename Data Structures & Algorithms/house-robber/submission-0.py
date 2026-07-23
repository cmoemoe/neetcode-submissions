#prices all positive, only get max by starting from house 0 or 1

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums) #reps max amt of money robbed at i
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        #if we rob house 1, dp[2] will be just the prev robed amount
        #dp[i-1]
        #or the robbed amount from two houses prior + itself
        #nums[i] + dp[i-2]

        #take max of these at each house
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        #max amt will be the final house val
        return dp[-1]
