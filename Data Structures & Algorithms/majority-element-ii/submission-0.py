class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        result = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for key, values in count.items():
            if values > len(nums) / 3:
                result.append(key)
        return result

        