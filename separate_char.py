def separate_characters(input_string, separator):
    separated_string = separator.join(input_string)
    return separated_string

# Example usage:
input_string = "Hello"
separator = "-"
result = separate_characters(input_string, separator)
print(result)
