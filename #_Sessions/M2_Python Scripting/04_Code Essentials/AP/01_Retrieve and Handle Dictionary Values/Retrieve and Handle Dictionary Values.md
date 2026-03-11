## 🎯 AP. Retrieve & Handle Dictionary Values

### Task Objective

In this task, you will:

* Organize code into modular Python scripts under a single project folder.
* Retrieve values from dictionaries using the `get()` method.
* Handle missing keys using default values.
* Access values from nested dictionaries using safe lookups.
* Count missing dictionary keys based on a required key list.
* Update dictionary values conditionally only if the key exists.
* Demonstrate how Python sets the `__name__` attribute when a module is run or imported.

### Folder Structure

```
dictionary_utils/
│
├── fetch_info.py
├── missing_data.py
├── update_stock.py
├── check_module.py
└── main_app.py
```

### Instructions

Create each of the following scripts inside the `dictionary_utils/` folder:

---

**`fetch_info.py`**

* Define a function `run_fetch_info()`.
* Inside the function:
  * Create a dictionary `employee` with keys: `"id"`, `"name"`, and `"department"`.
  * Use `.get()` to print the `"name"` value.
  * Try to retrieve `"location"` using `.get()` and provide `"Not Assigned"` as the default.
  * Add a nested `"contact"` dictionary inside `employee`.
  * Use chained `.get()` to safely access `"phone"`, defaulting to `"No Contact Provided"`.

---

**`missing_data.py`**

* Define a function `run_missing_data()`.
* Inside the function:
  * Create a dictionary `inventory` with keys such as `"item"` and `"price"`.
  * Define a list of required keys: `["item", "stock", "color"]`.
  * Count and print how many of the required keys are missing from `inventory`.

---

**`update_stock.py`**

* Define a function `run_update_stock()`.
* Inside the function:
  * Create a dictionary `product` with keys `"name"`, `"price"`, and `"stock"`.
  * Subtract `1` from `"stock"` using `.get()` with a fallback to `0`.
  * Print the updated dictionary.

---

**`check_module.py`**

* Define a function `run_check_module()`.
* Inside the function:
  * Print `"Executing check_module.py"`.
  * Print the value of `__name__`.

---

**`main_app.py`**

* Import all `run_*()` functions from the above modules.
* Call each function in sequence inside a `main()` function.
* Add the `if __name__ == "__main__"` block to run `main()` only when the file is executed directly.

---

### Sample Output

**▶️ Running Each Script Individually**

```bash
python fetch_info.py
```

```
Employee Name: Jake  
Location: Not Assigned  
Phone: No Contact Provided
```

```bash
python missing_data.py
```

```
Missing entries: 2
```

```bash
python update_stock.py
```

```
{'name': 'Laptop', 'price': 1200, 'stock': 9}
```

```bash
python check_module.py
```

```
Executing check_module.py  
Module name: __main__
```

---

**▶️ Running Full Project via main.py**

```bash
python main_app.py
```

```
Employee Name: Jake  
Location: Not Assigned  
Phone: No Contact Provided  

Missing entries: 2  

{'name': 'Laptop', 'price': 1200, 'stock': 9}  

Executing check_module.py  
Module name: check_module  

This is main_app.py. __name__ is: __main__
```
