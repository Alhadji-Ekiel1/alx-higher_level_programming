#!/usr/bin/python3

def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters that trigger new lines
    trigger_chars = ['.', '?', ':']

    # Initialize the result string
    result = ""

    # Iterate over each character in the text
    for char in text:
        # Add the character to the result
        result += char
        # If the character is a trigger character, add two new lines
        if char in trigger_chars:
            result += "\n\n"

    # Print the result
    print(result.strip())
