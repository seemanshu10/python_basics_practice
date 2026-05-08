"""
Converting toman numerals to integer 
"""

def romanToInt(S:str) -> int : 
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total=0
    prev = 0

    for char in reversed(S):
        curr = values[char]
        if curr < prev:
            total -= curr

        else:
            total +=curr
        prev = curr

    return total

string_input = input ("Input the Roman numerals:")
total=romanToInt(string_input)
print (total)
