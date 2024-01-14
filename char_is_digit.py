def is_digit(char_to_check):
    digits = '0123456789'
    return char_to_check in digits

# Example usage:
char_to_check = 'c'
if is_digit(char_to_check):
    print(f"'{char_to_check}' is a digit.")
else:
    print(f"'{char_to_check}' is not a digit.")
