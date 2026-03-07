#---------------- Read Mode ("r") -----------------------

# Create a sample file first
with open("file.txt", "w") as f:
    f.write("Hello World\nThis is a sample file.\n")


# Open the file in read mode
with open("file.txt", "r") as f:
    content = f.read()
    print("Reading file in 'r' mode:")
    print(content)



#---------------- Write Mode ("w") ----------------------

# Open file in write mode - overwrites existing content
with open("file.txt", "w") as f:
    f.write("This content overwrites the old file.\n")
    f.write("Second line in write mode.\n")


# Verify by reading
with open("file.txt", "r") as f:
    print("\nAfter 'w' mode (overwritten):")
    print(f.read())



#---------------- Append Mode ("a") ---------------------

# Open file in append mode - adds new data at the end
with open("file.txt", "a") as f:
    f.write("This line is appended.\n")
    f.write("Another appended line.\n")


# Verify by reading
with open("file.txt", "r") as f:
    print("\nAfter 'a' mode (appended):")
    print(f.read())
