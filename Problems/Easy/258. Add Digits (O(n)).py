class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            result = (num % 10) + num // 10
            if result < 10:
                return result
            num = result