## 🎯 AP. Random Password Generator - CLI

### Task Objective

In this task, you will:
* Build a CLI tool that generates a random password.
* Let users control password length and character types from command line arguments.
* Ensure the generated password includes at least one of each selected type.
* Handle invalid input such as missing arguments or short lengths.

### Instructions

* Create a Python script named `password_generator.py`.
* Accept the following command line arguments:
    * `--length <number>` (default: 8)
    * `--uppercase` to include uppercase letters
    * `--numbers` to include digits
    * `--special` to include special characters
* The script should:
    * Generate a random password using the selected options
    * Ensure at least one of each selected type is included
    * Use only lowercase letters if no options are given
    * If the length is too short for the selected options, show an error and exit
    * Print the final password to the terminal

---
### Sample Output

```
# Full option usage
$ python password_generator.py --length 12 --uppercase --numbers --special
Generated password: M8!akp#rLd2@
```

```
# Lowercase only (default behavior)
$ python password_generator.py --length 8
Generated password: qlrvtkam
```

```
# Invalid length value
$ python password_generator.py --length abc
Error: Invalid length value. Please provide a valid number.
```

```
# Length too short for selected types
$ python password_generator.py --length 2 --uppercase --numbers --special
Error: Password length too short for the specified criteria. Please increase the length.
```