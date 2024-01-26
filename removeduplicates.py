def remove_duplicates(string):
    unique_chars = ''.join(set(string))
    return unique_chars


string = "saaanket"
result = remove_duplicates(string)
print("String with duplicates removed:", result)
