# Creating a nested dictionary
employees = {
    "emp1": {"name": "John", "position": "Manager", "age": 35},
    "emp2": {"name": "Sara", "position": "Developer", "age": 28}
}


# ------------- Accessing Nested Elements -----------------
# Accessing the name of emp1
emp1_name = employees["emp1"]["name"]

# Accessing the position of emp2
emp2_position = employees["emp2"]["position"]


# -------------- Modifying Nested Dictionaries ----------------
student_info = {
    "John": {
        "age": 20,
        "major": "Computer Science"
    },
    "Alice": {
        "age": 22,
        "major": "Mathematics"
    }
}

# Modifying an inner element
student_info["John"]["major"] = "Data Science"

# Adding a new element in the inner dictionary
student_info["Alice"]["year"] = "Senior"

