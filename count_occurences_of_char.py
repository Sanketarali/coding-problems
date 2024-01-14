def count_occurrences(input_string, char_to_count):
    count = 0
    for char in input_string:
        if char == char_to_count:
            count += 1
    return count

# Example usage:
input_string = "Hello, World!"
char_to_count = "o"
occurrences = count_occurrences(input_string, char_to_count)
print(f"The character '{char_to_count}' appears {occurrences} times in the input string.")
