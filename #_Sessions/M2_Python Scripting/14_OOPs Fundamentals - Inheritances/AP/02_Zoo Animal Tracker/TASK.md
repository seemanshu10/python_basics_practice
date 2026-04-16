## AP. Zoo Animal Tracker with Method Overriding

### Task Objective

In this task, you will:

* Build a zoo animal tracker where different animal classes (like `Dog` and `Cat`) inherit from a parent class `Animal`.
* Each animal class will override the `sound()` method to demonstrate method overriding and make the tracker more interactive.

### Instructions

* Define a parent class named `Animal` with two methods:

  * `sound()` that prints a generic sound message.
  * `feeding_time()` that prints a generic feeding message.
* Create two child classes: `Dog` and `Cat`.
* Override the `sound()` method in each class to print a specific sound.
* Override the `feeding_time()` method in each class to print custom feeding instructions.
* Create one object of each class and call both methods on each object.

### Sample Output

**Usage**

```python
# Create objects and call methods
dog1 = Dog()
cat1 = Cat()

dog1.sound()
dog1.feeding_time()

cat1.sound()
cat1.feeding_time()
```

**Output**

```
The dog barks.
The dog eats twice a day.
The cat meows.
The cat eats once a day.
```
