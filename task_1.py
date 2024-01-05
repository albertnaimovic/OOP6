# Create a class method to return the factorial of a given number.


from math import factorial


class Factorial:
    @classmethod
    def get_factorial(cls, number: int) -> int:
        if number == 1:
            return number
        else:
            return number * factorial(number - 1)


print(Factorial.get_factorial(5))  # 120
