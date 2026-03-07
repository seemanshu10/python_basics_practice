## 🎯 AP. Library Book Inventory

### Task Objective

* Read a list of books from a JSON file.
* Calculate the total number of books per author.
* Save the results into a new JSON file.
* Ensure the program handles missing or unreadable input files gracefully.

### Instructions

Use a JSON file named `books.json` containing book records.

Write a Python script that:
* Loads the data from `books.json`.
* Aggregates book quantities per author.
* Saves the results into a file named `author_inventory.json`.
* Prints a confirmation message when done.
* Handle the case where the input file is not found and display an appropriate error message.

### Sample Output

Given this input file (`books.json`):

```
[
    {"title": "Book A", "author": "Author 1", "quantity": 5},
    {"title": "Book B", "author": "Author 2", "quantity": 3},
    {"title": "Book C", "author": "Author 1", "quantity": 7},
    {"title": "Book D", "author": "Author 3", "quantity": 2},
    {"title": "Book E", "author": "Author 2", "quantity": 4}
]
```

Your output file (`author_inventory.json`) should contain:

```
{
    "Author 1": 12,
    "Author 2": 7,
    "Author 3": 2
}
```

And the terminal should display:

```
Author inventory has been written to author_inventory.json.
```
