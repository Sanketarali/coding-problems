def sort_string(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string


string = "OpenAI"
result = sort_string(string)
print("Sorted string:", result)
