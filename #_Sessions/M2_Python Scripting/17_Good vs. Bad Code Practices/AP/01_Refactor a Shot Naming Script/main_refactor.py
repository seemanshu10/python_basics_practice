# Refactor Script

def validate_input(value, prefix):
    """
    Check if input is not empty and starts with the correct prefix.

    Args:
        value (str): The user-provided input.
        prefix (str): Expected prefix (e.g., 'SQ', 'SH', 'V').

    Returns:
        bool: True if valid, False otherwise.
    """
    if not value:
        return False
    
    value = value.upper()

    if value.startswith(prefix):
        return True
    else:
        return False

def generate_shot_name(sequence, shot, version):
    """
    Generate a formatted shot name.

    Args:
        sequence (str): Sequence identifier (e.g., SQ001).
        shot (str): Shot identifier (e.g., SH010).
        version (str): Version identifier (e.g., V003).

    Returns:
        str: Formatted shot name.
    """
    return f"{sequence.upper()}_{shot.upper()}_{version.upper()}"

def main():
    sequence = input("Enter sequence (e.g., SQ001): ").strip()

    if not validate_input(sequence, "SQ"):
        print("Error: Invalid sequence. It should start with 'SQ'.")
        return
    
    shot = input("Enter shot (e.g., SH010): ").strip()

    if not validate_input(shot, "SH"):
        print("Error: Invalid shot. It should start with 'SH'.")
        return
    
    version = input("Enter version (e.g., V003): ").strip()
    
    if not validate_input(version, "V"):
        print("Error: Invalid version. It should start with 'V'.")
        return

    shot_name = generate_shot_name(sequence, shot, version)
    print(f"Generated Shot Name: {shot_name}")

if __name__ == "__main__":
    main()