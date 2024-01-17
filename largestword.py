def find_largest_word(string):
    words = string.split() 
    largest_word = ''

    for word in words:
        if len(word) > len(largest_word):
            largest_word = word

    return largest_word


string = "Hello, this is a sample string to find the largest word."
result = find_largest_word(string)
print("Largest word:", result)
