class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = (j-i) * min(heights[i], heights[j])
                if area > max_res:
                    max_res = area

        return max_res

