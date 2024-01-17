def count_vowels_and_consonants(input_string):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    vowel_count = 0
    consonant_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return vowel_count, consonant_count

# Example usage:
input_string = "Hello, World!"
vowel_count, consonant_count = count_vowels_and_consonants(input_string)
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
