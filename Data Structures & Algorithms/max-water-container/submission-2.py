class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights)-1
        while l < r:
            num = min(heights[l], heights[r]) * (r-l)
            if ans < num:
                ans = num
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return ans

