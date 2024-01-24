def remove_chars(first_string, second_string):
    result = ""
    for char in first_string:
        if char not in second_string:
            result += char
    return result

first_string = "abed"
second_string = "cde"
result_string = remove_chars(first_string, second_string)
print(result_string)
