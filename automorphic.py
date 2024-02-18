def is_automorphic_number(num):
    # Calculate the square of the number
    square = num * num

    # Convert the number and its square to strings
    num_str = str(num)
    square_str = str(square)

    # Check if the number is present at the end of its square
    return square_str.endswith(num_str)

number = 5  # Replace with the number you want to check

if is_automorphic_number(number):
    print(f"{number} is an automorphic number.")
else:
    print(f"{number} is not an automorphic number.")
