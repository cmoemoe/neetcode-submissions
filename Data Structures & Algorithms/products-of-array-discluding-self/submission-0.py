import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        for i in range(len(nums)):
            if i == 0:
                pre = [1]
            else:
                pre = nums[:i]
            suff = nums[i + 1:]
            output.append((math.prod(pre)) * (math.prod(suff)))

        return output


