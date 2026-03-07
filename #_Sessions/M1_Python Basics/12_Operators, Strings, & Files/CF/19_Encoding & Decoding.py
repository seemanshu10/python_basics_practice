# ------------- Encoding
text = "Hello, world!"

encoded_text = text.encode("utf-8")
print(encoded_text)
print(type(encoded_text))

# b'Hello, world!'



# ------------- Decoding

decoded_text = encoded_text.decode("utf-8")
print(decoded_text)
print(type(decoded_text))
# Hello, world!




# Encode Decode
text = "Hello, πython!"

encoded = text.encode()
print("Encoded:", encoded)


decoded = encoded.decode("utf-8")
print("Decoded:", decoded)







# Which UTF Encoding Are We Using in Python?
text = "Hello 😊"

encoded = text.encode()
print(encoded)

# Output : b'Hello \xf0\x9f\x98\x8a'