## 🎯 AP. Employee Data Processing

### Task Objective

* Read structured employee data from a JSON file.
* Calculate the total salary for each department based on the input data.
* Write the results to a new JSON file in a readable format.
* Handle errors if the input file is missing or unreadable.

### Instructions

Use the provided `employees.json` file containing employee records.

Write a Python script that:
* Loads the data from `employees.json`.
* Aggregates salary totals per department.
* Saves the results into a new JSON file called `department_salaries.json`.
* Prints a confirmation message once the operation completes.
* Make sure your program handles the case where `employees.json` does not exist, and continues gracefully.

### Sample Output

Given this input file (`employees.json`):

```
[
    {"name": "Alice", "department": "Engineering", "salary": 70000},
    {"name": "Bob", "department": "HR", "salary": 50000},
    {"name": "Charlie", "department": "Engineering", "salary": 80000},
    {"name": "David", "department": "Marketing", "salary": 60000},
    {"name": "Eve", "department": "HR", "salary": 55000}
]
```

The output file (`department_salaries.json`) should contain:

```
{
    "Engineering": 150000,
    "HR": 105000,
    "Marketing": 60000
}
```

And the console should print:

```
Department salaries have been written to department_salaries.json.
```
