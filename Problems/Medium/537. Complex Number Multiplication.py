class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1 = num1.split("+")
        real2 = num2.split("+")
        imaginary1 = real1[1].split("i")
        imaginary2 = real2[1].split("i")
        realsol = int(real1[0]) * int(real2[0]) - int(imaginary1[0]) * int(imaginary2[0])
        print(int(imaginary1[0]), int(imaginary2[0]))
        imaginarysol = (int(real1[0]) * int(imaginary2[0])) + (int(imaginary1[0]) * int(real2[0]))
        return (str(realsol) + "+" + str(imaginarysol) + "i")
