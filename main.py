

 #***********************************************************
 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 #* Author = Ilyas Nayle
 #* P.I- Works Technical Assessment question
 #* Check divisibility of a given number by sum of its digits
 #* e.g = 75  = 7 + 5 = 12 and 75 is not divisible by 12
 #* e.g = 12 = 1 + 2 = 3 and 12 is divisible by 3

 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 #***********************************************************

class CheckDivisibility:
    @staticmethod
    def Abs_Value(num):
        if num < 0:
            return  -num
        return num

    def is_divisible(self, num):
        temp = self.Abs_Value(num)
        sum = 0

        while temp > 0:
            sum = sum + (temp % 10)
            temp = int ( temp / 10)

        if num % sum == 0:
            print(f"The sum of {num} is {sum}" )
            print(f"{num} is divisible {sum}")
            print("True")
        else:
            print(f"The sum of {num} is {sum}")
            print(f"{num} is not divisible {sum}")
            print("False")


def main():
    x = int(input("Enter a number: "))
    digits = CheckDivisibility()
    digits.is_divisible(x)


if __name__  == "__main__": main()


