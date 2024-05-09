class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        maxhap = 0
        temp = 0
        happiness.sort()
        for i in range(k):
            temp = happiness.pop() - i
            if temp < 0:
                temp = 0
            maxhap += temp
        return maxhap