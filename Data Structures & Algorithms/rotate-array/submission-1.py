class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Input: nums = [1,2,3,4,5,6,7,8], k = 4

        Brute Force: nums = [1,2,3,4,5,6,7,8]

        nums = [1,2,3,4,5,6,7,8]
        - reverse the array
        - [8,7,6,5,4,3,2,1]
        - [5,6,7,8,4,3,2,1]
        - [5,6,7,8,1,2,3,4]
        """
        nums.reverse()
        modulo = k % len(nums)
        nums[:modulo] = reversed(nums[:modulo])
        nums[modulo:] = reversed(nums[modulo:])
        return nums

        


        