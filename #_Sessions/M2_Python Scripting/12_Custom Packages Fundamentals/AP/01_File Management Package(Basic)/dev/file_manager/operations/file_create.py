
def create_file(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")