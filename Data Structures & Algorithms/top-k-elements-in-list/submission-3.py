class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        #values = []
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        frequency = sorted(counter, key = counter.get, reverse = True) [0:k]
        return frequency


        