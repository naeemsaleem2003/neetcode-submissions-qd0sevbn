class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {}    
        hashmap[0] = 1
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in hashmap:
                count += hashmap[prefix_sum - k]
            if prefix_sum in hashmap:
                hashmap[prefix_sum] += 1
            else:
                hashmap[prefix_sum] = 1
        return count