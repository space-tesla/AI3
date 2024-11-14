# Q.1 Write a Python program to remove punctuations from the given string.

def remove_punctuation(input_string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in input_string:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct

input_string = input("Enter a string with punctuation: ")

print("String without punctuation:", remove_punctuation(input_string))



Output:
Enter a string with punctuation: Hello, world!
String without punctuation: Hello world