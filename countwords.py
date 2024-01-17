def count_words(string):
    words = string.split()
    return len(words)


string = "Hello, how are you?"
result = count_words(string)
print("Number of words:", result)
