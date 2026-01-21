"""
 takes two string inputs from the user and checks 
if the two strings are anagrams of each other. An anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# logic : 
check if length is same if not then no point to check whether ,not anagram 
but if same length could be but check is it 
so go thehough each character of first string and remove that character in second strings if any character is nnot in str 2 it is not anagram  

"""

# taking input from user 

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# If lengths differ, not anagrams
if len(str1) != len(str2):
    print("Not anagrams")
else:
    
    list1 = list(str1)
    list2 = list(str2)

    for ch in list1:
        if ch in list2:
            list2.remove(ch)
        else:
            print("Not anagrams")
            break
    else:
        print("Anagrams")
