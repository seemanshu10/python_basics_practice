'''
## 🎯 AP. Counting Vowels in a Sentence Using Loops

### Task Objective

In this task, you will:
* Use loops to iterate through characters in a string.
* Apply conditional logic to detect and count vowels.
* Strengthen character-based iteration and string handling skills.


### Instructions
* Take a sentence input from the user.
* Convert the sentence to lowercase for consistent comparison.
* Use a loop to check each character one by one.
* Count how many vowels (`a`, `e`, `i`, `o`, `u`) appear in the sentence.
* Print the total number of vowels found.
> ✅ Use only basic loop and conditional logic to solve this task.
> ❌ Do not use built-in functions like `count()` to get the result directly.

### Sample Output

```
Enter a sentence: Learning Python is fun
Total vowels: 6
```

'''

# user input of String 

user_Input = input("Enter A sentence : ").lower()

# also first converting to lowercase 

words= user_Input.lower()

print(words)
# count_vowel 
vowel_count =0

for char in words:
    if char =='a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowel_count += 1 # increment the counter if the character is a vowel 

# print total number of vowels 
print("Total Values: ", vowel_count)

"""
Enter A sentence : Learning Python is fun
learning python is fun
Total Values:  6
"""