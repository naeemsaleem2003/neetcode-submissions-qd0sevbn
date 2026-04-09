class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Input: word1 = "abc", word2 = "xyz"
        Output: "axbycz"
        
        """
        new_string = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                new_string.append(word1[i])
            if i < len(word2):
                new_string.append(word2[i])
            i += 1
        final_string = "".join(new_string)
        return final_string
            
        