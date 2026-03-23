def display_shots(shots):
    print("Shot List:")

    for shot in shots:
        print(f"- {shot['name']} ({shot['status']})")