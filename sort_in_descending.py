def sort_characters_descending(input_string):
    # Use sorted() to sort the characters in descending order
    sorted_string = ''.join(sorted(input_string, reverse=True))
    return sorted_string

# Example usage:
input_string = "programming"
result = sort_characters_descending(input_string)
print(result)
