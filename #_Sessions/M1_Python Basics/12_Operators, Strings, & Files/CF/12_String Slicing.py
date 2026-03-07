#---------------- Basic slicing [start:end] ----------------


# print(word[0:6])   # Output: Develo (characters from index 0 to 5)


# # print(word[:5])  #
# # print(word[1:])

# # print(word[1:13])
# # print(word[:9:])

# print(word[::2])

# print(word[::-3])

word = "Developer"

print(word[-9:-4:2])












# #---------------- Slicing with step [start:end:step] --------
# message = "Technology"

# print(message[0:10:3])  # Output: Tnl (characters from index 0 to 9, step 3)



# #---------------- Omit start [:end] ------------------------
# greeting = "HelloWorld"

# print(greeting[:5])    # Output: Hello (from start to index 4)



# #---------------- Omit end [start:] ------------------------
# language = "JavaScript"

# print(language[4:])    # Output: Script (from index 4 to end)



# #---------------- Negative indexing [-n:-m] -----------------
# framework = "DjangoFramework"

# print(framework[-8:-4])  # Output: rame (from index -8 to -5)



# #---------------- Reverse string [::-1] --------------------
# platform = "OpenAI"

# print(platform[::-1])  # Output: IAnepO (entire string reversed)