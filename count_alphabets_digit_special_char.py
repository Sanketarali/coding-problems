def count_alphabets_digits_special_chars(input_string):
    alphabets = digits = special_chars = 0

    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special_chars += 1

    return alphabets, digits, special_chars

# Example usage:
input_string = "Hello, 123 World!"
alphabets, digits, special_chars = count_alphabets_digits_special_chars(input_string)
print(f"Alphabets: {alphabets}")
print(f"Digits: {digits}")
print(f"Special Characters: {special_chars}")
