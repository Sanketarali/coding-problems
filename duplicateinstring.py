def find_duplicates(string):
    duplicates = []

    for char in string:
        if string.count(char) > 1 and char not in duplicates:
            duplicates.append(char)

    return duplicates


my_string = "Hellooooss, World!"
result = find_duplicates(my_string)
print("Duplicates:", result)
