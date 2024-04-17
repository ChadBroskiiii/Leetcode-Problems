class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numdict = {}
        for num in nums:
            if num in numdict:
                numdict[num] += 1
                return True
            else:
                numdict[num] = 1
        return False