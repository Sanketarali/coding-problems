def remove_character(input_string, char_to_remove):
    # Use the replace method to remove the specified character
    result_string = input_string.replace(char_to_remove, '')
    return result_string

# Example usage:
input_string = "Hello, World!"
char_to_remove = "o"

result = remove_character(input_string, char_to_remove)

print(f"String after removing '{char_to_remove}': {result}")
