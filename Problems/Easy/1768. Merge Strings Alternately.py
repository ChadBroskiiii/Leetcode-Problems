class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        if len(word1) >= len(word2):
            for i in range(len(word1)):
                try:
                    string += word1[i]
                    string += word2[i]
                except IndexError:
                    pass
            return string
        else:
            for i in range(len(word2)):
                try:
                    string += word1[i]
                    string += word2[i]
                except IndexError:
                    string += word2[i]
            return string