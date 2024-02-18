def is_armstrong_number(num):
    # Calculate the number of digits in num
    num_str = str(num)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of num_digits
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if num is equal to the sum of its digits raised to the power of num_digits
    return num == digit_sum

num = 153  # Replace with the number you want to check

if is_armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
