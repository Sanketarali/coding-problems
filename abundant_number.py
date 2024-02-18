def is_abundant_number(num):
    # Calculate the sum of proper divisors
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    
    # Check if the sum of proper divisors is greater than the number itself
    return divisor_sum > num

number = 12  # Replace with the number you want to check

if is_abundant_number(number):
    print(f"{number} is an abundant number.")
else:
    print(f"{number} is not an abundant number.")
