class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        create hashmap (counter):
            - increment count of char in s
            - decrement count for char in t
            - if hashmap chars = 0, return true. Else false
        """
        # create hashmap
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) - 1
        for val in count.values():
            if val != 0:
                return False
        return True
    
        