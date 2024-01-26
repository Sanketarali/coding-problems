def reverse_words(string):
    words = string.split()
    reversed_string = ' '.join(words[::-1])
    return reversed_string


string = "Hello, how are you?"
result = reverse_words(string)
print("Reversed string:", result)
