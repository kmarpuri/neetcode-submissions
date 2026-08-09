class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        count = 0
        for num in nums:
            if target-num in visited:
                return [visited[target-num], count]
            if num not in visited:
                visited[num] = count
            count+=1
        return [-1, -1]
