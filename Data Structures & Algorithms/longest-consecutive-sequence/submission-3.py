class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        best = 0

        for x in seen:
            # only start counting if x is the start of a sequence
            if x - 1 not in seen:
                curr = x
                streak = 1

                while curr + 1 in seen:
                    curr += 1
                    streak += 1

                best = max(best, streak)

        return best
        