class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = {}
        for i, j in enumerate(nums):
            complement = target - j
            if complement in solution:
                return [solution[complement], i]
            solution[j] = i

        
        