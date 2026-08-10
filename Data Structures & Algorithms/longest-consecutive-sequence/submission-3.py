class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = sorted(list(set(nums)))
        count = 0
        maxCount = count
        prev = 0
        for v in visited:
            print(v)
            if count == 0:
                prev = v
                count+=1
                maxCount = count
            else:
                if v - 1 == prev:
                    prev = v
                    count+=1
                    if count > maxCount:
                        maxCount = count
                else:
                    prev = v
                    count = 1
        return maxCount
            