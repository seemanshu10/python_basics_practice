# -----------Write Binary File(wb)
data = b"Hello Binary World!"  
print(type(data))

with open("example.txt", "wb") as file:
    file.write(data)

print("Data written successfully.")



# ------------ Read Binary File(rb)
with open("sample.bin", "rb") as file:
    read = file.read()
    print(type(read))

    # print(data)
    print(read[:4])

with open("red.png", "rb") as file:
    iread = file.read()
    print(type(iread))

    # print(data)
    print(iread[:4])

# Output: b'Hello, Binary World!'




# # -------------- Appending to a Binary File (ab)
more_data = b" Appending some bytes."

with open("sample.bin", "ab") as file:
    file.write(more_data)


print("Data appended successfully.")

# # Output: Data appended successfully.