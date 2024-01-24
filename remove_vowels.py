def remove_vowels(input_string):
    vowels = 'aeiouAEIOU'  # Define a string containing all vowels
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result

# Example usage:
input_string = "Hello, World!"
result = remove_vowels(input_string)
print(result)
