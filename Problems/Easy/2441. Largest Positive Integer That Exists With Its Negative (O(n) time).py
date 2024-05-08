class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        tempmax = 0
        for i in range(len(nums)):
            if abs(nums[i]) > tempmax:
                if nums[i] < 0:
                    if abs(nums[i]) in nums:
                        tempmax = abs(nums[i])
                elif nums[i] > 0:
                     if -nums[i] in nums:
                        tempmax = abs(nums[i])
        
        if tempmax == 0:
            return -1
        else:
            return tempmax