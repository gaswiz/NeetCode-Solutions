#Solution 1

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


#Solution 2: 

# from typing import List

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()  
        
#         for n in nums: 
#             if n in hashset:  
#                 return True 
#             hashset.add(n) 
        
#         return False 
