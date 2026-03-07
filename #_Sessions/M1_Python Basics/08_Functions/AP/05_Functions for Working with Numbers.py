"""
# Description of the Task:
In this extended task, you will create additional functions to perform more operations on a list of numbers. You will write functions to sort the list, reverse the list, and find the median of the list. You will also create a function to check if a number is prime.

# Instructions:
Write a function sort_numbers(numbers) that takes a list of numbers and returns a new list with the numbers sorted in ascending order.
Write a function reverse_numbers(numbers) that takes a list of numbers and returns a new list with the numbers in reverse order.
Write a function find_median(numbers) that takes a list of numbers and returns the median of the numbers.
Write a function is_prime(number) that takes a single number and returns True if the number is prime, and False otherwise.

# Learning Objective:
Deepen understanding of how to define and use functions in Python.
Practice advanced list operations within functions.
Improve problem-solving skills by implementing sorting and searching algorithms.
Learn how to determine if a number is prime.

# Sample Usage and Expected Output:
numbers = [10, 15, 20, 25, 30]
print(sort_numbers(numbers))         # Output: [10, 15, 20, 25, 30]
print(reverse_numbers(numbers))      # Output: [30, 25, 20, 15, 10]
print(find_median(numbers))          # Output: 20
print(is_prime(29))                  # Output: True
print(is_prime(30))                  # Output: False
"""


def sort_numbers(numbers):
    """
    Returns a new list with numbers sorted in ascending order.   
    """
    return sorted(numbers)


def reverse_numbers(numbers):    
    """
    Returns a new list with numbers in reverse order.  
    """
    return numbers[::-1]       


def find_median(numbers):
    """
    Returns the median of a list of numbers.     
    """
    sorted_nums = sorted(numbers)   
    n = len(sorted_nums)    

    if n == 0:
        return None

    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2     
    else:
        return sorted_nums[mid]     
 

def is_prime(number):
    """
    Returns True if the number is prime, otherwise False.
    """
    if number <= 1: 
        return False

    for i in range(2, int(number ** 0.5) + 1):  
        if number % i == 0:
            return False    

    return True

numbers = [10, 15, 20, 25, 30]
print(sort_numbers(numbers))
print(reverse_numbers(numbers))
print(find_median(numbers))
print(is_prime(29))  
print(is_prime(30))
  
"""
[10, 15, 20, 25, 30]
[30, 25, 20, 15, 10]
20
True
False
"""