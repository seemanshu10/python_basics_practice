## 🎯 AP. Working with Dates and Times

### Task Objective

In this task, you will:

* Perform operations using the `datetime` and `timedelta` classes.
* Work with dates, times, intervals, formatting, and date arithmetic.
* Use this knowledge to solve real-world scheduling and time-handling scenarios.

---

### Subtask 1: Calculate the Number of Days Between Two Dates

**Instruction**
Input two dates in the format `YYYY-MM-DD`. Calculate and return the number of days between them.

**Sample Usage and Expected Output**

```python
date1 = "2024-01-01"
date2 = "2024-07-22"
# Output
202
```

---

### Subtask 2: Format a Date to DD/MM/YYYY

**Instruction**
Convert a date from the format `YYYY-MM-DD` to `DD/MM/YYYY`.

**Sample Usage and Expected Output**

```python
date = "2024-07-22"
# Output
22/07/2024
```

---

### Subtask 3: Add Seconds to a Given Time

**Instruction**
Input a time in `HH:MM:SS` format and a number of seconds. Return the new time.

**Sample Usage and Expected Output**

```python
time = "12:30:15"
seconds_to_add = 3600
# Output
13:30:15
```

---

### Subtask 4: Calculate Age from Birthdate

**Instruction**
Input a birthdate in the format `YYYY-MM-DD`. Return the person's age in years (based on today’s date).

**Sample Usage and Expected Output**

```python
birthdate = "1990-07-22"
# Output
34  # Assuming today is 2024-07-22
```

---

### Subtask 5: Determine the Day of the Week for a Given Date

**Instruction**
Input a date in the format `YYYY-MM-DD`. Return the day of the week.

**Sample Usage and Expected Output**

```python
date = "2024-07-22"
# Output
Monday
```

---

### Subtask 6: Find Time Difference Between Two Times

**Instruction**
Input two times in `HH:MM:SS` format. Return the difference between them in hours, minutes, and seconds.

**Sample Usage and Expected Output**

```python
time1 = "12:30:15"
time2 = "14:45:30"
# Output
2:15:15
```

---

### Subtask 7: Generate a List of Dates Within a Given Range

**Instruction**
Input start and end dates in `YYYY-MM-DD` format. Return a list of all dates in that range (inclusive).

**Sample Usage and Expected Output**

```python
start_date = "2024-07-01"
end_date = "2024-07-05"
# Output
['2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04', '2024-07-05']
```

---

### Subtask 8: Count Number of Weekend Days in a Date Range

**Instruction**
Input start and end dates in `YYYY-MM-DD` format. Return the total number of weekend days (Saturday and Sunday).

**Sample Usage and Expected Output**

```python
start_date = "2024-07-01"
end_date = "2024-07-31"
# Output
9
```

---

### Subtask 9: Generate Time Intervals Within a Day

**Instruction**
Input a start time, end time in `HH:MM` format, and an interval in minutes. Return a list of time intervals.

**Sample Usage and Expected Output**

```python
start_time = "09:00"
end_time = "12:00"
interval = 30
# Output
['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00']
```

---

### Subtask 10A: Get Date After a Given Number of Days from Today

**Instruction**
Input a number of days. Return the date that many days from today.

**Sample Usage and Expected Output**

```python
days = 30
# Output
2024-08-21  # Assuming today is 2024-07-22
```

---

### Subtask 10B: Get Date Before a Number of Days from a Given Date

**Instruction**
Input a date and number of days. Return the earlier date.

**Sample Usage and Expected Output**

```python
date = "2024-07-22"
days = 15
# Output
2024-07-07
```

---

### Subtask 10C: Determine if a Year is a Leap Year

**Instruction**
Input a year. Return `True` if it is a leap year, else `False`.

**Sample Usage and Expected Output**

```python
year = 2024
# Output
True
```
