def is_valid_shot_code(shotCode):
    """
    Checks the shot code validity . 
    - Can start with 'SH'. 
    - Shot code should be only digits and can only be till 3 digits

    This function check and return False and True according to checks .
    """
    shotCode = shotCode.upper()
    if not shotCode.startswith("SH"):
        print("Shot Code Can only start with (SH).")
        return False
    
    number_part_shot = shotCode[2:]
    
    if not number_part_shot.isdigit():
        print("Shot Code should be all digits not characters.")
        return False
    
    if len(number_part_shot) <= 3:
        return True
    else:
        print("Error: Invalid shot number length given. Only less than equal to 3 shot number allowed like (001)")
        return False
    
def is_valid_status(new_status):

    ALLOWED_STATUS = ["not_started", "in_progress", "review", "approved", "hold"]

    if new_status not in ALLOWED_STATUS:
        return False

    return True

def is_valid_shot_status_filter(filter_status):
    ALLOWED_FILTERS = {None, "--done", "--pending", "--review"}

    # Validate filter once
    if filter_status not in ALLOWED_FILTERS:
        print("Wrong filter given. Only Allowed Filters are [done |pending | review]")
        return False
    
    return True

if __name__ == "__main__":
    outCode = is_valid_shot_code("sh0010")
    print(f"Output: {outCode}")