def sort_characters_ascending(input_string):
    # Use sorted() to sort the characters in ascending order
    sorted_string = ''.join(sorted(input_string))
    return sorted_string

# Example usage:
input_string = "programming"
result = sort_characters_ascending(input_string)
print(result)
