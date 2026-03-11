def run_missing_data():
    inventory = {
        "item" : 'Laptop',
        "price" : 25520
    }

    # list of reuired keys 
    inventory_keys = ["item", "stock", "color"]
    
    # countin missing keys 
    missing_key_count = 0
    for key in inventory_keys:
        if key not in inventory:
            missing_key_count += 1

    print("Number if missing required keys:", missing_key_count)


if __name__ == "__main__":
    run_missing_data()
