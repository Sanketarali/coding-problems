def find_non_repeating_chars(string):
    non_repeating_chars = []
    for char in string:
        if string.count(char) == 1:
            non_repeating_chars.append(char)
    return non_repeating_chars

string = input("Enter a string: ")
non_repeating_chars = find_non_repeating_chars(string)
print("Non-repeating characters:", non_repeating_chars)