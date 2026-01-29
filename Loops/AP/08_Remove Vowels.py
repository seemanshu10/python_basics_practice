"""
program that removes all vowels from a given string input by the user and prints the modified string.


"""
# enter a userInput 
user_Input = input("Enter A string : ")

# vowels Definition
vowels = "aeiouAEIOU"

# create empty string to store the result 
result_str =""
# loop each characrted and check if it is vowels i not add in result if is skip it 

for char in user_Input:
    # check if vowels 
    if char not in vowels:
        result_str+=char
# print the result 
print("Strings Without Vowels:",result_str)

"""
Enter A string : I love this Python.
Strings Without Vowels:  lv ths Pythn.

Enter a string: Hello World
Modified string: Hll Wrld
"""