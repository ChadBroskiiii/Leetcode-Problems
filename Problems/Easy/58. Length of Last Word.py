class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversed = s[::-1]
        split = reversed.split(" ")
        for i in range(len(split)):
            if split[i] != '':
                return len(split[i])
