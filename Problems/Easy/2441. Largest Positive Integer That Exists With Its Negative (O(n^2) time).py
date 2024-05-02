class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        tempmax = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == -nums[j] or -nums[i] == nums[j]:
                    if abs(nums[i]) > tempmax:
                        tempmax = nums[i]
        if tempmax == 0:
            return -1
        else:
            return tempmax