class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        result = right   
        while left <= right:
            mid = (left + right) // 2
            needed_days = 1
            curr = 0
            for w in weights:
                if curr + w <= mid:
                    curr += w
                else:
                    needed_days += 1
                    curr = w
            if needed_days <= days:
                result = mid        
                right = mid - 1     
            else:
                left = mid + 1      
        return result