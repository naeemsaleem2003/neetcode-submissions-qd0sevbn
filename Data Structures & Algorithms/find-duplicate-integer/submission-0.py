class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for val, count in counter.items():
            if count > 1:
                return val
        