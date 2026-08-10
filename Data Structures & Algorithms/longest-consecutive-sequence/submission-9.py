class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)

        maxCount = 0

        for num in nums:
            if num - 1 in visited:
                continue
            count = 1
            cur = num + 1
            while cur in visited:
                cur+=1
                count+=1
            maxCount = max(maxCount, count)

        return maxCount
            