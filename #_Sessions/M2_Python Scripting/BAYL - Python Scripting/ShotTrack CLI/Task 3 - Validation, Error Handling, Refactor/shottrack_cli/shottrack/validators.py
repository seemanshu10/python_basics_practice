def is_valid_code(shot_code):

    if not shot_code.startswith("SH"):
        print("Error: Shot should only Start with SH")
        return False
    
    number_part = shot_code[2:]
    # print(number_part)
    
    if len(number_part) < 3:
        print("Error: Shot should be padded with 3 digits.")
        return False
    
    if not number_part.isdigit():
        print("Error: Shot should be padded with only digits.")
        return False
    

    return True

if __name__ == "__main__":
    out_code = is_valid_code("sh100")
    print(out_code)