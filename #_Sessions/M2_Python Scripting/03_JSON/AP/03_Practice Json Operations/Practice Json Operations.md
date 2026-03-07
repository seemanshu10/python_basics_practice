## 🎯 AP. Practice JSON Operations

### Task Objective

* Load and manipulate structured JSON data stored in a file.
* Practice accessing, modifying, adding, and removing elements within JSON data.
* Save the modified JSON to a new file after processing.
* Apply proper error handling for file operations and JSON parsing.

### Instructions

Create a JSON file named `person.json` and insert the following data:

```
{
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Wonderland",
        "postalCode": "12345"
    },
    "phoneNumbers": [
        {"type": "home", "number": "555-1234"},
        {"type": "work", "number": "555-5678"}
    ]
}
```

Then, create a Python script named `json_operations.py` and complete the subtasks below in order.

### 🧩 Subtask 1: Load JSON Data

* Load data from the `person.json` file using `json.load()`.
* Handle `FileNotFoundError` if the file is missing.
* Handle `json.JSONDecodeError` if the file contains invalid JSON.

### 🧩 Subtask 2: Access Simple Key-Value Pairs

* Access the values of `"name"` and `"age"` from the JSON data.
* Print them in the format:
  `Name: Alice, Age: 30`

### 🧩 Subtask 3: Access Nested Objects

* Access `"street"` and `"city"` inside the `"address"` object.
* Print them in the format:
  `Street: 123 Main St, City: Wonderland`

### 🧩 Subtask 4: Access Elements in an Array

* Access both elements in the `"phoneNumbers"` list.
* Print the phone numbers in the format:
  `Home Phone: 555-1234, Work Phone: 555-5678`

### 🧩 Subtask 5: Modify JSON Data

* Change `"age"` to `31`.
* Update the `"city"` in `"address"` to `"New Wonderland"`.
* Append a new phone number object:
  `{"type": "mobile", "number": "555-9876"}`

### 🧩 Subtask 6: Add New Elements

* Add `"email": "alice@example.com"` to the root level of the JSON.
* Add `"country": "Wonderland"` inside the `"address"` object.

### 🧩 Subtask 7: Remove Elements

* Remove the `"postalCode"` field from `"address"`.
* Remove the first entry from the `"phoneNumbers"` list (the home number).

### 🧩 Subtask 8: Save to File

* Save the modified JSON object to a new file named `output.json` using `json.dump()`.
* Use proper error handling for file writing.

### Sample Output

Console output:

```
Name: Alice, Age: 30  
Street: 123 Main St, City: Wonderland  
Home Phone: 555-1234, Work Phone: 555-5678  
Modified JSON saved to output.json  
```

Output written to `output.json`:

```
{
    "name": "Alice",
    "age": 31,
    "address": {
        "street": "123 Main St",
        "city": "New Wonderland",
        "country": "Wonderland"
    },
    "phoneNumbers": [
        {
            "type": "work",
            "number": "555-5678"
        },
        {
            "type": "mobile",
            "number": "555-9876"
        }
    ],
    "email": "alice@example.com"
}
```
