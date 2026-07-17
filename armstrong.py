n = int(input("Enter a number: "))

num_str = str(n)
num_digits = len(num_str)

sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

if sum_of_powers == n:
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")
