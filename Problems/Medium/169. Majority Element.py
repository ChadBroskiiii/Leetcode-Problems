import statistics
from statistics import mode

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return mode(nums)