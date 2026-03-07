with open("sample.bin", "rb+") as file:
    original = file.read()

    print("Original content:", original)

    file.seek(0)
    file.write(b"Hi")
    


with open("sample.bin", "rb") as file:
    print("Modified content:", file.read())
    

'''
# Output: 
    # Original content: b'Hello, Binary World!'
    # Modified content: b'Hillo, Binary World!'
'''