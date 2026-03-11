def run_fetch_info():

    # Create a dictionary employee
    employee = {
        "id": 101,
        "name": "Jake",
        "department": "HR"
    }

    # Use .get() to print the "name" value
    print("Name:", employee.get("name"))

    # Retrieve "location" with default value
    print("Location:", employee.get("location", "Not Assigned"))

    # Add a nested "contact" dictionary
    employee["contact"] = {
        "phone": "9876543210",
        "email": "alice@example.com"
    }
    #print(employee)

    # Safely access "phone" using chained .get()
    phone = employee.get("contact", {}).get("phone", "No Contact Provided")
    print("Phone:", phone)
    
if __name__ == "__main__":
    run_fetch_info()