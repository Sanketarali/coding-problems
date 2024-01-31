import re

def sum_numbers_in_string(string):
    numbers = re.findall(r'\d+', string)

    total_sum = sum(int(num) for num in numbers)

    return total_sum

string = "123xyz"
result = sum_numbers_in_string(string)
print("Sum of numbers in the string:", result)
