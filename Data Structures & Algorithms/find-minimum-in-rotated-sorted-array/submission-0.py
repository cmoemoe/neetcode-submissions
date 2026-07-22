class Solution:
    def findMin(self, nums: List[int]) -> int:
        #bin search?
        #if mid > hi, move lo to mid [3, 4, 5, 6, 1, 2]
        #if mid < lo, move hi to mid [5, 6, 1, 2, 3, 4]
        if len(nums) == 1:
            return nums[0]

        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) //2
            if nums[mid] < nums[hi]: #in order, min is in the left portion
                hi = mid
            else:
                lo = mid + 1
        
        return nums[lo]


        
