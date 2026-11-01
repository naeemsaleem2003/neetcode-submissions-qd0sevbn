class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        - initialize container to store sequences
        - check if integer is start of sequence
        - add and increment accordingly
        """
        num_set = set(nums)
        counter = 0
        #curr_counter = 0
        for i in num_set:
            if i - 1 not in num_set:
                curr_counter = 1
                current = i
                while current + 1 in num_set:
                    curr_counter += 1
                    current += 1
                counter = max(counter, curr_counter)
        return counter

                

        