class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        vals = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        frequency = sorted(counts, key=counts.get, reverse=True)
        return frequency[:k]