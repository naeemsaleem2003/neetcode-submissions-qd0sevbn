class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        postfix = 1
        for num in range(len(nums)):
            output[num] = prefix
            prefix *= nums[num]
        for num in range(len(nums) -1, -1, -1):
            output[num] *= postfix
            postfix *= nums[num]
        return output