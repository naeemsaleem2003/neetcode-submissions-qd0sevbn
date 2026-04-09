class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if j > i + 1 and b == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    four_sum = a + b + nums[left] + nums[right]
                    if four_sum < target:
                        left += 1
                    elif four_sum > target:
                        right -= 1
                    else:
                        result.append([a, b, nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right :
                            left += 1
        return result