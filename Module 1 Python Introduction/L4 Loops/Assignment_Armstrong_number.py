#armstrong number that equals the sum of its own digits raised to the power of the number of digits. example as 153= 1**3(3), 5**3(125), 3**3(27)


num = input("Enter a number: ")

original = num
digits = len(num)
total = 0

for digit in num:
    total += int(digit) ** digits

if total == int(original):
    print("Armstrong number")
else:
    print("Not an Armstrong number")