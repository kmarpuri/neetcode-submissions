class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        maxCount = 0

        for num in nums:
            if num - 1 in visited:
                continue
            count = 1
            next = num + 1
            while next in visited:
                next+=1
                count+=1
            maxCount = max(maxCount, count)

        return maxCount
            