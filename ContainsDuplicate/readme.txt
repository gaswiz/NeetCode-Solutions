# NeetCode Problem Solving: Contains Duplicate

This repository contains solutions to the "Contains Duplicate" problem, designed to check if a given list of numbers contains any duplicate elements. The solutions use Python to demonstrate efficient problem-solving techniques.

---

## Problem Description

**Input:** A list of integers, `nums`.  
**Output:** A boolean value indicating whether any value appears at least twice in the list.  

---

## Solutions

### Solution 1: Function-Based Approach
This approach uses a Python function with a `set` to track seen numbers. If a number is already in the `set`, the function immediately returns `True` as a duplicate exists.

**Code**:
```python
def hasDuplicate(nums):
    hashset = set()  # Initialize an empty set
    
    for n in nums:
        if n in hashset:  # If n is already in the set, it's a duplicate
            return True
        hashset.add(n)  # Otherwise, add n to the set
    
    return False  # No duplicates found

# Test cases
print(hasDuplicate([1, 2, 3, 3]))  # Output: True
print(hasDuplicate([1, 2, 3, 4]))  # Output: False