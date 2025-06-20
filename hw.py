def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join them back into a string
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Example usage
input_string = "Hello world this is Python"
reversed_string = reverse_words(input_string)
print("Original:", input_string)
print("Reversed word by word:", reversed_string)