"""
program that counts the number of words in a given text file.

# Instructions:
Prompt the user to enter the name of the text file they want to analyze.
Open the specified file in read mode.
Read the contents of the file.
Split the contents into words using whitespace as the delimiter.
Count the number of words.
Print the total word count to the console.
"""
#  user input for the file name
file_name = input("Enter the name of the text file: ")

input_file = open(f"FileHandling/AP/{file_name}", "r")
content = input_file.read()
print (content)
input_file.close()

 # Split the contents into words using whitespace
words = content.split()

# Count the number of words
word_count = len(words)

# Print the result
print("Total number of words:", word_count)

"""

Enter the name of the text file: input.txt
John
Alice
Bob
Charlie
Total number of words: 4
"""