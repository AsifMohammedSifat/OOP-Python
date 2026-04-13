class Calculator:
    def add(self, *nums):
        return sum(nums)


calc = Calculator()

print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 20))


# Example 02
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(5))        # 5
print(calc.add(5, 10))    # 15
print(calc.add(5, 10, 20)) # 35