data = b"Hello, Binary World!"  

# print(type(data))

# with open("sample.bin", "wb") as f:
#     f.write(data)




# # --------- Reading an Image File
with open("sample.bin", "rb") as f:
    content = f.read()

print(content)
print(type(content))


# <class 'bytes'>
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01'