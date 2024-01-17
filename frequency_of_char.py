def calculate_character_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

string = "Hello, World!"
result = calculate_character_frequency(string)
print(result)
