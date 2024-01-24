def remove_char(input_string, char_to_remove):
    result = ""
    for char in input_string:
        if char != char_to_remove:
            result += char
    return result

# Example usage:
input_string = "Hello, World!"
char_to_remove = "o"
result = remove_char(input_string, char_to_remove)
print(result)  # Output: Hell, Wrld!
