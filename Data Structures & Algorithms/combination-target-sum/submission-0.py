class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        #brute force is summing each idx with all idx options
        #until min mult as many times as possible > target
        #will give us dups

        #create tree, root.left = nums[0], root.right = nums[all except 0]
        #continue where node.left = another nums[0], root.right = no more nums[0]
        #conitnue until reaching sum > target

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy()) #copy curr
                return
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop() #remove if we include combo
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
        
