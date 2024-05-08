class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        string = str(x)
        list1 = []
        sumnum = 0
        for i in range(len(string)):
            list1.append(string[i])

        for i in range(len(list1)):
            sumnum += int(list1[i])
        
        if x % sumnum == 0:
            return sumnum
        else:
            return -1